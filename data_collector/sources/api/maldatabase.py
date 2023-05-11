import requests
import logging
from requests import HTTPError
from data_collector.classes import FeedCollector
from data_collector.helpers import csv_to_json
from django.conf import settings

logger = logging.Logger(__name__)

class Maldatabase(FeedCollector):

    base_url = 'https://api.maldatabase.com'
    maldatabase = requests.Session()

    def __init__(self):
       super().__init__(self.__class__.__name__)
        
    
    def init_collector(self):
          self.headers = {
            "Authorization": self.secrets["api_key"],
            "Accept-Encoding": "gzip, deflate"
        }
    
    def collect(self):
        try:
            final_url = self.base_url + "/download"
            response = self.maldatabase.get(final_url,headers=self.headers)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
        return csv_to_json(response.text)
    
    def collect_target(self, target):
        pass