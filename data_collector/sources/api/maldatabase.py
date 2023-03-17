import os
import logging
import requests
from requests import HTTPError
from data_collector.classes import Collector

logger = logging.Logger(__name__)

class Maldatabase(Collector):

    base_url = 'https://api.maldatabase.com/'
    maldatabase = requests.Session()

    def __init__(self):
         self.headers = {
            "Authorization": os.getenv("MALDATABASE_API_KEY"),
        }
        
    
    def init_collector(self):
        return super().init_collector()

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