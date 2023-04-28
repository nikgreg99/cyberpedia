import logging
import requests
from requests import HTTPError
from data_collector.classes import Collector
from django.conf import settings

logger = logging.getLogger(__name__)

class ThreatJammer(Collector):

    base_url : str = "https://dublin.api.threatjammer.com/v1"
    threat_jammer = requests.Session()

    def __init__(self):
       super().__init__(self.__class__.__name__)

    def init_collector(self):
        api_key = self.secrets["api_key"]
        self.headers = {
            'Accept': "application/json",
            "Authorization": "Bearer {}".format(api_key)
        }
        self.threat_jammer.proxies = settings.PROXIES

    def request_threat_jammer(self,final_url,parameters = None):
        try:
            response = self.pulsidive.get(final_url,params=parameters,headers=self.headers)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
        return response.json()
    

    def collect(self):
         final_url = self.base_url + "/source/ip"
         return self.request_threat_jammer(final_url)
    
    def collect_target(self, target):
        pass
