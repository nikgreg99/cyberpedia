import requests
import logging
from requests import HTTPError
from data_collector.classes import Collector
from django.conf import settings

logger = logging.Logger(__name__)

class Maldatabase(Collector):

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
            print(response.content)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
        return response.content
    
    def collect_target(self, target):
        pass