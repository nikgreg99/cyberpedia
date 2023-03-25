import logging
import requests
from requests import HTTPError
from data_collector.classes import Collector
from data_collector.utils import validate_hash


logger = logging.getLogger(__name__)

class ThreatFox(Collector):

    base_url = 'https://threatfox-api.abuse.ch/api/v1/'
    threat_fox = requests.Session() 


    def __init__(self) -> None:
       super().__init__(self.__class__.__name__) 

    def init_collector(self):
        self.api_key = self.secrets["api_key"]


    def _make_threat_fox_request(self,requests_data):
        try:
            recent_ioc_response = self.threat_fox.post(self.base_url,data=requests_data)
            recent_ioc_response.raise_for_status()
        except HTTPError as ex:
            pass
        return recent_ioc_response.json()

    def _query_recent_IOC(self):
        data = {
            "query": "get_iocs",
            "days": 7
        }
        return self._make_threat_fox_request(data)
    
    def _search_IOC_by_target(self,target):
        data = {
            "query": "search_ioc",
            "search_term": target
        }
        return self._make_threat_fox_request(data)
    
    def _search_IOC_by_hash(self,hash):
        data = {
            "query": "search_by_hash",
            "hash": hash
        }
        return self._make_threat_fox_request(data)

    def _query_malware(self,malware, limit=100): 
        data = {
            "query:": "malwareinfo",
            "malware": malware,
            "limit": limit
        }      
        return self._make_threat_fox_request(data)
    
    def get_malware_list(self):
        data = {
            "query": "malware_list"
        }
        return self._make_threat_fox_request(data)
    
    def collect(self):
        return super().collect()
    
    def collect_target(self, target):
        return super().collect_target(target)


