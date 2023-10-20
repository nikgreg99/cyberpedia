import logging
import requests
from requests import HTTPError
from data_collector.classes import TargetCollector
from data_collector.utils import is_ip
from data_collector.exceptions import InvalidIPAddressFormat
from django.conf import settings

logger = logging.getLogger(__name__)

class IPApi(TargetCollector):

    base_url : str = "https://ipapi.co/api" 
    ipapi = requests.Session()

    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance = super(IPApi,cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        self.init_collector()
        

    def init_collector(self):
        self.ipapi.proxies = settings.PROXIES
        self.error = {}
    
    def make_requests(self,final_url):
        try:
            response = self.ipapi.get(final_url)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
            self.error['ipapi'] = ex
        return response.json()


    def collect_target(self,target) -> dict:
        if is_ip(target):
            final_url = self.base_url + f"/{target}/json"
            data = self.make_request(final_url=final_url)
            return data   


