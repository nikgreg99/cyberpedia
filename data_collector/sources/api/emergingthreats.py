import requests
from requests import HTTPError
import logging
from data_collector.classes import Collector

logger = logging.getLogger(__name__)

class EmergingThreats(Collector):

    base_url: str = "https://api.emergingthreats.net/v1"
    emerging_threats = requests.Session()

    def __init__(self) -> None:
        super().__init__(__class__.__name__)

    def init_collector(self):
        self.headers = {
            'Authorization': self.secrets["api_key"]
        }

    
    

    
    