import os
import logging
import requests
from requests import HTTPError
from django.conf import settings
from data_collector.classes import Collector
from django.conf import settings

logger = logging.getLogger(__name__)

class Yarify(Collector):

    base_url : str = "https://yaraify-api.abuse.ch/api/v1/"
    download_url : str = "https://yaraify-api.abuse.ch/download/"
    yarify =  requests.Session()

    def __init__(self):
       super().__init__(self.__class__.__name__)

    def init_collector(self):
        self.yarify.proxies = settings.PROXIES


    def list_recent_deployed_rules(self):
        data = {
             "query" : "recent_yararules"
         }
        try:
             response  = self.yarify.post(self.base_url,json=data)
             response.raise_for_status()
        except HTTPError as ex:
             logging.error("Error requesting Yara rules ")
        return response.json()


    def download_Yara_rulset(self):
        os.chdir(settings.YARA_DIR)
        try:
            response = self.yarify.get(self.base_url)
            response.raise_for_status()
        except HTTPError as ex:
            logging.exception(ex)
            


