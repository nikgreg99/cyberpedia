import logging
import requests
from requests import HTTPError
from data_collector.classes import TargetCollector
from django.conf import settings

logger = logging.getLogger(__name__)


class Whois(TargetCollector):

    base_url : str = "https://www.whoisxmlapi.com/whoisserver/WhoisService"
    session = requests.Session()

    def __init__(self) -> None:
       super().__init__(self.__class__.__name__)
    
    def init_collector(self):
        self.api_key = self.secrets["api_key"]
        self.params = {
            "apiKey": self.api_key,
            "outputFormat": "JSON",
            "preferFresh": 1,
            "ip": 1,
            "ipWhois": 1
        }
        self.session.proxies = settings.PROXIES
      
    def collect_target(self,target: str):
        self.params["domainName"] = target
        try:
            response =  self.session.get(self.base_url,params=self.params)
            response.raise_for_status()
        except HTTPError as ex:
            logger.error(ex)
        return response.json()

    