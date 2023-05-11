import logging
import requests
from requests import HTTPError
from data_collector.classes import TargetCollector
from django.conf import settings

logger = logging.getLogger(__name__)

class Pulsedive(TargetCollector):

    base_url: str = "https://pulsedive.com/api"
    base_url_info : str = base_url + "/info.php"
    pulsidive = requests.Session()

    def __init__(self) -> None:
       super().__init__(self.__class__.__name__)

    def init_collector(self):
        self.api_key = self.secrets["api_key"]
        self.pulsidive.proxies = settings.PROXIES
       
    def make_pulsidve_request(self,final_url,parameters):
        try:
            response = self.pulsidive.get(final_url,params=parameters)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
        return response.json()

    def get_indicator_by_value(self,target):
        parameters = {
            "key": self.api_key,
            "pretty": 1,
            "indicator": target
        }    
        return self.make_pulsidve_request(self.base_url_info,parameters)
    

    def get_threat_by_name(self,threat):
        parameters = {
            "key": self.api_key,
            "pretty": 1,
            "indicator": threat
          }
        return self.make_pulsidve_request(self.base_url_info,parameters)
    
    def collect_target(self, target):
        return self.get_threat_by_name(target)

    