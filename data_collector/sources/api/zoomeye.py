import logging
import requests
from requests import HTTPError
from data_collector.classes import TargetCollector
from django.conf import settings

logger = logging.getLogger(__name__)


class ZoomEye(TargetCollector):
    
    base_url : str = "'https://api.zoomeye.org"
    zoomeye = requests.Session()

    def __init__(self) -> None:
       super().__init__(self.__class__.__name__)
       self.init_collector()

    def init_collector(self):
        api_key = self.secrets["api_key"]
        self.zoomeye.headers = {
            "API-KEY" : api_key
        }
        self.zoomeye.proxies = settings.PROXIES
    
    def collect_target(self, target):
        try:
            final_url = self.base_url + "/host/searchs"
            query = {
                'query' : f'ip:{target}'
            }
            response =  self.zoomeye.get(final_url,params=query)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
        return response.json()


    

