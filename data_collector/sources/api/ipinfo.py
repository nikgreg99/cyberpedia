import logging
import requests
from requests import HTTPError
from data_collector.classes import TargetCollector
from data_collector.utils import validate_ip_address
from django.conf import settings

logger = logging.getLogger(__name__)

class IPInfo(TargetCollector):
    
    api_key = None
    base_url = "https://ipinfo.io"
    ipinfo = requests.Session()

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        self.init_collector()
        self.error = {}


    def init_collector(self):
        self.headers = {
            "Accept": "application/json",
            "Authorization": "Bearer {}".format(self.secrets["api_key"])
        }
        self.ipinfo.proxies = settings.PROXIES
        

    def ip_info(self,ip):
        final_url = self.base_url + f"/{ip}"
        try:
            response = self.ipinfo.get(final_url,headers=self.headers)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
            self.error["ipinfo"] = ex
        return response.json()
        
    def collect_target(self, target):
        if validate_ip_address(target):
            data = self.make_request(target)
        return data

      



        

   