import logging
import requests
from requests import HTTPError
from data_collector.classes import Collector
from data_collector.utils import validate_ip_address
from data_collector.exceptions import InvalidIPAddressFormat

logging = logging.getLogger(__name__)

class IPInfo(Collector):
    
    api_key = None
    base_url = "https://ipinfo.io"
    ipinfo = requests.Session()

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)


    def init_collector(self):
        self.headers = {
            "Accept": "application/json",
            "Authorization": "Bearer {}".format(self.secrets["api_key"])
        }
        

    def ip_info(self,ip):
        if validate_ip_address(ip):
            final_url = self.base_url + "/{}".format(ip)
            try:
                response = self.ipinfo.get(final_url,headers=self.headers)
                response.raise_for_status()
            except HTTPError as ex:
                logging.error("Error executing request")
            return response.json()
        else:
            raise InvalidIPAddressFormat("This IP is not supported")


      



        

   