import os
import requests
import logging
from requests import HTTPError
from data_collector.classes import Collector

logger = logging.Logger(__name__)

class Maldatabase(Collector):

    base_url = 'https://api.maldatabase.com/'
    maldatabase = requests.Session()

    def __init__(self):
       super().__init__(self.__class__.__name__)
        
    
    def init_collector(self):
          print(self._secrets)
          self.headers = {
            "Authorization": self._secrets["api_key"]
        }

    def collect(self):
        try:
            final_url = self.base_url + "download"
            response = self.maldatabase.get(final_url,headers=self.headers)
            response.raise_for_status()
        except HTTPError as ex:
            logger.error("Error request")
        return response.json()
    
    def collect_target(self, target):
        return super().collect_target(target)