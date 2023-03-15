import logging
import requests
from requests import HTTPError
import enum
from data_collector.classes import Collector

logger = logging.getLogger(__name__)

class WhoisOutputFormatType(enum):
    XML = "XML"
    JSON = "JSON"

class Whois(Collector):

    base_url : str = "https://www.whoisxmlapi.com/whoisserver/WhoisService"
    session = requests.Session()
    
    def _init_(self):
        self.api_key = ""
        self.params = {
            "apiKey": self.api_key,
            "outputFormat": WhoisOutputFormatType.JSON,
            "preferFresh": 1,
            "ip": 1,
            "ipWhois": 1
        }
      
    def collect_target(self,target: str):
        self.params["domainName"] = target
        try:
            response =  self.session.get(self.base_url,params=self.params)
            response.raise_for_status()
        except HTTPError as ex:
            logger.error("Error executing request")

    