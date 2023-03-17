import requests
from requests import HTTPError
import logging
from data_collector.classes import Collector
from data_collector.utils import validate_ip_address

logger = logging.getLogger(__name__)

class Maltiverse(Collector):

    base_url: str = "https://api.maltiverse.com"
    maltiverse = requests.Session()


    def init_collector(self):
        return super().init_collector()
    
    def collect(self):
        return super().collect()
    
    def collect_target(self, target):
        return super().collect_target(target)