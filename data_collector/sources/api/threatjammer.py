import logging
import requests
from requests import HTTPError
from data_collector.classes import FeedCollector
from django.conf import settings

# Probably to discard
logger = logging.getLogger(__name__)


class ThreatJammer(FeedCollector):

    base_url: str = "https://dublin.api.threatjammer.com/v1"
    threat_jammer = requests.Session()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ThreatJammer, cls).__new__(cls)
        return cls.instance


    def __init__(self):
       super().__init__(self.__class__.__name__)
       self.init_collector()

    def init_collector(self):
        api_key = self.secrets["api_key"]
        self.threat_jammer.headers = {
            'Accept': "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        self.error = {}
        self.threat_jammer.proxies = settings.PROXIES

    def make_request(self, final_url="", params={}, data={}):
        try:
            response = self.threat_jammer.get(final_url,params=params)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
            self.error['threatjammer'] = ex
        return response.json()
    

    def collect(self):
         final_url = self.base_url + "/source/ip"
         return self.make_request(final_url=final_url)
    
