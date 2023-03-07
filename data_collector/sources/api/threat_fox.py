import requests
from data_collector.exceptions import ErrorRequestException

MD5_CHARACTERS = 32
SHA256_CHARACTERS = 64

class ThreatFox():

    base_url: str = "https://threatfox-api.abuse.ch/api/v1"
    threat_fox = requests.Session() 
    api_key = None   

    def set_parameters():
        pass


    def _make_threat_fox_request(self,data):
        try:
            recent_ioc_response = requests.post(self.base_url,data=data)
            recent_ioc_response.raise_for_status()
        except ErrorRequestException as ex:
            pass
        return recent_ioc_response.json()

    def _query_recent_IOC(self):
        data = {
            "query": "get_iocs",
            "days": 7
        }
        return self._make_threat_fox_request(data)
    
    def _serch_IOC_by_target(self,target):
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


