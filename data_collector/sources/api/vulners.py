import requests
from requests import HTTPError
from data_collector.classes import Collector

class Vulners(Collector):

    base_url : str = "https://vulners.com/api/v3"
    vulners = requests.Session()

    def init_collector(self):
        return super().init_collector()
    
    def collect(self):
        return super().collect()
    
    def collect_target(self, target):
        return super().collect_target(target)