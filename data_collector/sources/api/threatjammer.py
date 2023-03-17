import logging
import requests
from requests import HTTPError
from data_collector.classes import Collector

logger = logging.getLogger(__name__)

class ThreatJammer(Collector):

    base_url : str = "https://dublin.api.threatjammer.com"
    threat_jammer = requests.Session()


    def init_collector(self):
        return super().init_collector()
    

    def collect(self):
        return super().collect()
    
    def collect_target(self, target):
        return super().collect_target(target)