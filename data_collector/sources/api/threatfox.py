import logging
import requests
from requests import HTTPError
from data_collector.classes import FeedCollector
from data_collector.utils import validate_hash
from django.conf import settings


logger = logging.getLogger(__name__)

class ThreatFox(FeedCollector):

    base_url = 'https://threatfox-api.abuse.ch/api/v1/'
    threat_fox = requests.Session() 

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ThreatFox, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
       super().__init__(self.__class__.__name__) 
       self.init_collector()

    def init_collector(self):
        self.api_key = self.secrets["api_key"]
        self.threat_fox.proxies = settings.PROXIES
        self.error = {}

    def make_request(self, final_url="", params={}, data={}):
        try:
            response = self.threat_fox.post(self.base_url,json=data)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
            self.error['threatfox'] = ex
        return response.json()

    def collect_recent_IOC(self):
        data = {

            "query": "get_iocs",
            "days": 7
        }
        return self.make_request(data=data)

    
    def collect_malware_info(self):
        data = {
            "query": "malware_list"
        }
        return self.make_request(data=data)
    
    def collect(self):
        ioc = self.collect_recent_IOC()
        malware = self.collect_malware_info()
        return {
            'ioc': ioc,
            'malware-list': malware
        }



