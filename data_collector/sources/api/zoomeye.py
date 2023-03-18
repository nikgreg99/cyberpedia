import logging
import requests
from requests import HTTPError
from data_collector.classes import Collector

logger = logging.getLogger(__name__)


class ZoomEye(Collector):
    
    zoomeye = requests.Session()

    def init_collector(self):
        api_key = self._secrets["api_key"]
        return super().init_collector()
    

