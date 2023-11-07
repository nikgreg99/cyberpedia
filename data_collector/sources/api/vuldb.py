import logging
import requests
from requests import HTTPError
from data_collector.classes import  FeedCollector
from django.conf import settings

logger = logging.getLogger(__name__)

class VulDB(FeedCollector):
    base_url : str = "https://vuldb.com/?api"
    vuldb = requests.Session()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(VulDB, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        self.init_collector()

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
