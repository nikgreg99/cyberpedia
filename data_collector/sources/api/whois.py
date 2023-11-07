import logging
import requests
from requests import HTTPError
from data_collector.classes import TargetCollector
from django.conf import settings

logger = logging.getLogger(__name__)


class Whois(TargetCollector):

    base_url : str = "https://www.whoisxmlapi.com/whoisserver/WhoisService"
    whois = requests.Session()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Whois, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
       super().__init__(self.__class__.__name__)
       self.init_collector()
    
    def init_collector(self):
        self.err = {}
        self.api_key = self.secrets["api_key"]
        self.params = {
            "apiKey": self.api_key,
            "outputFormat": "JSON",
            "preferFresh": 1,
            "ip": 1,
            "ipWhois": 1
        }
        self.whois.proxies = settings.PROXIES
      
    def collect_target(self,target: str):
        self.params["domainName"] = target
        try:
            response =  self.whois.get(self.base_url,params=self.params)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
            self.err['whois']= ex
        return response.json()

    