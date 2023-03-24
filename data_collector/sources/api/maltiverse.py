import requests
from requests import HTTPError
import logging
from data_collector.classes import Collector
from data_collector.utils import validate_ip_address

logger = logging.getLogger(__name__)

class Maltiverse(Collector):

    base_url: str = "https://api.maltiverse.com"
    maltiverse = requests.Session()

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def init_collector(self):
       pass
    
    def collect(self):
        pass
    
    def collect_target(self, target):
        pass