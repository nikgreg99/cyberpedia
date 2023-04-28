import requests
from requests import HTTPError
import logging
from data_collector.classes import Collector
from data_collector.utils import validate_ip_address
from data_collector.exceptions import InvalidIPAddressFormat
from django.conf import settings

logger = logging.getLogger(__name__)

class Greynoise(Collector):

    base_url : str = "https://api.greynoise.io/v3"
    greynoise = requests.Session()

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def init_collector(self):
        self.headers = {
            'Key': self.secrets["api_key"]
        }
        self.greynoise.proxies = settings.PROXIES
       
    
    def collect_target(self, target):
        if validate_ip_address(target):
            final_url = self.base_url +  "/community/{}".format + target
            try:
                response = self.greynoise.get(final_url,headers=self.headers)
                response.raise_for_status()
            except HTTPError as ex:
                logger.exception(ex)
            return response.json()
            