import logging
import json
import requests
import time
from ratelimit import limits
from requests import HTTPError
from data_collector.classes import TargetCollector
from data_collector.utils import is_url
from data_collector.exceptions import UnsupportedTarget
from django.conf import settings

logger = logging.getLogger(__name__)

class UrlScan(TargetCollector):

    base_url : str = "https://urlscan.io/api/v1"
    urlscan = requests.Session()
    api_key = None

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
            "API-KEY" : self.secrets["api_key"]
        }
        self.urlscan.proxies = settings.PROXIES

    @limits(calls=60,period=60)
    def submit_url(self,target):
        if is_url(target):
            data = {
                'url':target,
                'visibility': 'public'
            }
            try:
                final_url = self.base_url + "/scan"
                response = self.urlscan.post(final_url,data=json.dumps(data))
                response.raise_for_status
            except HTTPError as ex:
                logger.exception(ex)
            return response.json()
        else:
            raise UnsupportedTarget(f"The {target} cannot be analyzed")

    @limits(calls=60,period=60)
    def get_url_report(self,submission_response):
        if 'uuid' in submission_response:
            uuid = submission_response["uuid"]
            final_url = self.base_url + f"/result/{uuid}"
            data : dict = {
                "visibility": "public",
                "uuid": uuid
            }
            max_tries = 10
            poll_distance = 2
            time.sleep(10)
            for chanche in range(max_tries):
                if chanche:
                    time.sleep(poll_distance)
                response = self.urlscan.get(final_url,headers=self.headers,data=json.dumps(data))
                if response.status_code == 404:
                    continue
                result = response.json()
                break
            return result
        else:
            logger.error("Non field uuid present in submission_URL responsnse")

    def collect_target(self,target) -> dict:
        response = self.submit_url(target)
        report = self.get_url_report(response)
        return report