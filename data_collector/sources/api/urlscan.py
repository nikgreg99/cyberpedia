import json
import requests
import logging
from requests import HTTPError
from data_collector.classes import Collector
from django.conf import settings

logger = logging.getLogger(__name__)

class UrlScan(Collector):

    base_url : str = "https://urlscan.io/api/v1"
    urlscan = requests.Session()
    api_key = None


    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def init_collector(self):
        self.headers: dict = {
            "Content-Type ": "application/json",
            "API-KEY" : self.secrets["api_key"]
        }
        self.urlscan.proxies = settings.PROXIES
       

    def submit_url(self,url):
        data : dict = {
            "visibility": "public",
            "url": url
        }
        final_url = self.base_url + "/scan"
        try:
            response = self.urlscan.post(final_url,headers=self.headers,data=json.dumps(data))
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception("Failing submission URL")
        return response.json()
        
    def get_url_report(self,url,submission_response):
        if 'uuid' in submission_response:
            uuid = submission_response["uuid"]
            final_url = self.base_url + "/result/{}".format(uuid)
            data : dict = {
                "visibility": "public",
                "uuid": uuid
            }
            try:
                response = self.urlscan.get(final_url,headers=self.headers,data=json.dumps(data))
                response.raise_for_status()
            except HTTPError as ex:
                logger.exception("Failed executing request")
        else:
            logger.error("Non field uuid present in submission_URL responsnse")
