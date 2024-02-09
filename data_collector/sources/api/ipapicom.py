import requests
import logging
from requests import HTTPError
from data_collector.classes import TargetCollector
from data_collector.utils import is_IP_adress
from django.conf import settings

logger = logging.getLogger(__name__)

class IPApiCom(TargetCollector):

    base_url: str = "https://api.ipapi.com/api"
    ipapi_com = requests.Session()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(IPApiCom, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        self.init_collector()

    def init_collector(self):
        self.error = {}
        self.ipapi_com.params = {
            "access_key": self.secrets["api_key"]
        }
        self.ipapi_com.proxies = settings.PROXIES

    def make_request(self, final_url="", params={}, data={}):
        try:
            response = self.ipapi_com.get(final_url)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
            self.error["ipapi.com"] = ex
        return response.json()
    

    def collect_target(self,target) -> dict:
        if is_IP_adress(target):
            final_url = self.base_url + f"/{target}"
            data = self.make_request(final_url)
        return data

