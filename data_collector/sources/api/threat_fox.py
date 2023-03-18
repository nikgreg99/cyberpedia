import logging
import requests
from requests import HTTPError
from data_collector.classes import Collector

MD5_CHARACTERS = 32
SHA256_CHARACTERS = 64

logger = logging.getLogger(__name__)

class ThreatFox(Collector):

    base_url = 'https://threatfox-api.abuse.ch/api/v1/'
    threat_fox = requests.Session() 
    api_key = None   

    def init_collector(self):
        self.api_key = self._secrets["api_key"]


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


