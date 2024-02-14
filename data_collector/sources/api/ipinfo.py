import logging
import requests
from requests import HTTPError
from data_collector.classes import TargetCollector
from data_collector.utils import is_IP_adress
from django.conf import settings

logger = logging.getLogger(__name__)

#STATUS OK
class IPInfo(TargetCollector):
    
    api_key = None
    base_url = "https://ipinfo.io"
    ipinfo = requests.Session()

    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance = super(IPInfo,cls).__new__(cls)
        return cls.instance


    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        self.init_collector()
        self.error = {}


    def init_collector(self):
        self.ipinfo.headers = {
            "Accept": "application/json",
            "Authorization": "Bearer {}".format(self.secrets["api_key"])
        }
        self.ipinfo.proxies = settings.PROXIES
        

    def make_request(self, final_url="", params={},data={}):
        try:
            response = self.ipinfo.get(final_url,headers=self.ipinfo.headers)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
            self.error["ipinfo"] = ex
        return response.json()
        
    def collect_target(self, target):
        if is_IP_adress(target):
            final_url = self.base_url + f"/{target}"
            data = self.make_request(final_url)
        return data

      



        

   