import logging
import requests
from requests import HTTPError
from data_collector.classes import Collector
from django.conf import settings

logger = logging.getLogger(__name__)

class VulDB(Collector):
    base_url : str = "https://vuldb.com/?api"
    vuldb = requests.Session()

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def init_collector(self):
        api_key = self.secrets["api_key"]
        self.vuldb.proxies = settings.PROXIES
        self.vuldb.headers = {
            'X-VulDB-ApiLKey': api_key
        }
    
    def collect(self):
        return super().collect()
    

    def collect_target(self, target):
        return super().collect_target(target)
