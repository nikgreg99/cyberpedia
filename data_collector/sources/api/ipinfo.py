import logging
import requests
from requests import HTTPError
from data_collector.classes import Collector
from data_collector.utils import validate_ip_address
from data_collector.exceptions import InvalidIPAddressFormat
from django.conf import settings

logger = logging.getLogger(__name__)

class IPInfo(Collector):
    
    api_key = None
    base_url = "https://ipinfo.io"
    ipinfo = requests.Session()

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        self.ipinfo.proxies = settings.PROXIES


    def init_collector(self):
        self.headers = {
            "Accept": "application/json",
            "Authorization": "Bearer {}".format(self.secrets["api_key"])
        }
        

    def ip_info(self,ip):
        final_url = self.base_url + "/{}".format(ip)
        try:
            response = self.ipinfo.get(final_url,headers=self.headers)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
        return response.json()
        
    def collect_target(self, target):
        return self.ip_info(target)

      



        

   