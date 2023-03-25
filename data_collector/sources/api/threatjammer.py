import logging
import requests
from requests import HTTPError
from data_collector.classes import Collector


logger = logging.getLogger(__name__)

class ThreatJammer(Collector):

    base_url : str = "https://dublin.api.threatjammer.com"
    threat_jammer = requests.Session()

    def __init__(self):
       super().__init__(self.__class__.__name__)

    def init_collector(self):
        pass
    

    def collect(self):
        return super().collect(self)
    
    def collect_target(self, target):
        return super().collect_target(target)