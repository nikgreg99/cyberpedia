import requests
from requests import HTTPError
import logging
from data_collector.classes import TargetCollector
from data_collector.exceptions import UnsupportedTarget
from data_collector.utils import is_IP_adress
from django.conf import settings

logger = logging.getLogger(__name__)


# STATUS: OK
class Greynoise(TargetCollector):

    base_url : str = "https://api.greynoise.io/v3"
    greynoise = requests.Session()

    def __new__(cls):
     if not hasattr(cls, 'instance'):
        cls.instance = super(Greynoise, cls).__new__(cls)
     return cls.instance

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        self.init_collector()
        
    def init_collector(self):
        self.err = {}
        self.greynoise.headers = {
            'Key': self.secrets["api_key"],
            'accept': "application/json"
        }
        self.greynoise.proxies = settings.PROXIES

    def make_request(self, final_url="", params={}, data={}):
        try:
            response = self.greynoise.get(final_url)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
        return response.json()
       
    
    def collect_target(self, target):
        if is_IP_adress(target):
            final_url = self.base_url +  f"/community/{target}"
            response = self.make_request(final_url=final_url)
            return response
        else:
            raise UnsupportedTarget(f"{target} target is not supported")

            