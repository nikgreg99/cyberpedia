import logging
import requests
from requests import HTTPError
from data_collector.classes import TargetCollector,FeedCollector
from data_collector.utils import validate_hash
from django.conf import settings


logger = logging.getLogger(__name__)

class ThreatFox(FeedCollector,TargetCollector):

    base_url = 'https://threatfox-api.abuse.ch/api/v1/'
    threat_fox = requests.Session() 


    def __init__(self) -> None:
       super().__init__(self.__class__.__name__) 

    def init_collector(self):
        self.api_key = self.secrets["api_key"]
        self.threat_fox.proxies = settings.PROXIES


    def make_request(self, final_url="", params=..., data=...):
        try:
            response = self.threat_fox.post(self.base_url,json=data)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
        return response.json()

    def query_recent_IOC(self):
        data = {
            "query": "get_iocs",
            "days": 7
        }
        return self.make_request(data=data)
    
    def search_IOC_by_target(self,target):
        data = {
            "query": "search_ioc",
            "search_term": target
        }
        return self.make_request(data=data)
    
    def search_IOC_by_hash(self,hash):
        data = {
            "query": "search_by_hash",
            "hash": hash
        }
        return self.make_request(data=data)

    def query_malware(self,malware, limit=100): 
        data = {
            "query:": "malwareinfo",
            "malware": malware,
            "limit": limit
        }      
        return self._make_request(data=data)
    
    def get_malware_list(self):
        data = {
            "query": "malware_list"
        }
        return self.make_request(data=data)
    
    def collect(self):
        return self.query_recent_IOC(),self.get_malware_list()
    
    def collect_target(self, target):
        return super().collect_target(target)


