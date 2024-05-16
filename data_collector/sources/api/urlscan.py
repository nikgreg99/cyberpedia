import logging
import json
import requests
import time
from requests import HTTPError
from data_collector.classes import TargetCollector
from data_collector.utils import is_url
from data_collector.exceptions import UnsupportedTarget
from django.conf import settings

logger = logging.getLogger(__name__)


class UrlScan(TargetCollector):

    BASE_URL: str = "https://urlscan.io/api/v1"
    urlscan = requests.Session()
    scan_type: str
    visibility: str


    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(UrlScan, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        self.init_collector()

    def init_collector(self):
        self.err = {}
        self.urlscan.headers = {
            "Content-Type ": "application/json",
            "API-KEY": self.secrets["api_key"]
        }
        self.urlscan.proxies = settings.PROXIES

    def make_get_request(self,final_url,params={},data={}):
        try:
            response = self.urlscan.get(final_url, headers=self.headers,
                                        params=params,data=data)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
        return response

    def search(self,target):
        final_url = self.BASE_URL + "/search"
        query_params = {
            'q': f"domain:{target}"
        }
        response = self.make_get_request(final_url=final_url,params=query_params)
        return response

    def submit_url(self, target):
        if is_url(target):
            data = {
                'url': target,
                'visibility': 'public'
            }
            try:
                final_url = self.BASE_URL + "/scan"
                response = self.urlscan.post(final_url,data=json.dumps(data))
                response.raise_for_status
            except HTTPError as ex:
                logger.exception(ex)
            return response.json()
        else:
            raise UnsupportedTarget(f"The {target} cannot be analyzed")

    """
      After the submission the API suggest to make a poll each 10-30 seconds
      until the response is obtained or a  maximum is reached
    """
    def get_url_report(self, submission_response):
        if 'uuid' in submission_response:
            uuid = submission_response["uuid"]
            final_url = self.BASE_URL + f"/result/{uuid}"
            data: dict = {
                "visibility": "public",
                "uuid": uuid
            }
            max_tries = 10
            poll_distance = 2
            time.sleep(10)
            for chanche in range(max_tries):
                if chanche:
                    time.sleep(poll_distance)
                response = self.make_get_request(final_url, data=json.dumps(data))
                if response.status_code == 404:
                    continue
                result = response.json()
                break
            return result
        else:
            logger.error("Non field uuid present in submission_URL responsnse")

    def collect_target(self, target) -> dict:
        response = self.submit_url(target)
        report = self.get_url_report(response)
        return report