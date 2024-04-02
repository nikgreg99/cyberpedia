import logging
import requests
from enum import Enum
from requests import HTTPError
from data_collector.classes import TargetCollector
from data_collector.utils import is_IP_adress
from data_collector.exceptions import UnsupportedTarget
from django.conf import settings

logger = logging.getLogger(__name__)


class ZoomeEyeParameter(Enum):
    IP = "ip"
    PORT = "port"


class ZoomEye(TargetCollector):
    
    base_url : str = "https://api.zoomeye.org"
    zoomeye = requests.Session()

    def __init__(self) -> None:
       super().__init__(self.__class__.__name__)
       self.init_collector()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ZoomEye, cls).__new__(cls)
        return cls.instance

    def init_collector(self):
        api_key = self.secrets["api_key"]
        self.zoomeye.headers = {
            "API-KEY": f"{api_key}"
        }
        self.error = {}
        self.zoomeye.proxies = settings.PROXIES

    def make_request(self, final_url="", params={}):
        try:
            response =  self.zoomeye.get(final_url,params=params)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
            self.error['zoomeye'] = ex
        return response.json()
    
    def collect_target(self, target):
        if is_IP_adress(target): 
             final_url = self.base_url + "/host/search"
             query = {
                'query' : f'ip:{target}'
              }
             return self.make_request(final_url,params=query)
        else:
            raise UnsupportedTarget(f'{target} is not valid')

          


    

