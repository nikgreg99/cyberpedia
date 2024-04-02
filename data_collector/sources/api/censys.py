import requests
from requests import HTTPError
from data_collector.classes import TargetCollector
from data_collector.utils import ip_address
import logging
from django.conf import settings

logger = logging.getLogger()

class Censys(TargetCollector):
    
    base_url = "https://search.censys.io/api/"
    censys = requests.Session()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Censys, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        self.init_collector()
        self.error = {}        

    def init_collector(self):
        secret = self.secrets["secret"]
        api_key = self.secrets["api_key"]
        self.censys.headers = {
            'accept': 'application/json',
            'Secret': secret, 
            'API ID': api_key
        }
        self.censys.proxies = settings.PROXIES

    def make_request(self, final_url="", params={}, data={}):
        try:
            response = self.censys.get(final_url)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
        return response.json()

    def collect_target(self, target):
        if ip_address(target):
            final_url = self.base_url + f"v2/hosts/{target}"
            return self.make_request(final_url=final_url)

        

    