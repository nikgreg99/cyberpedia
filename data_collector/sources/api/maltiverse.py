import requests
from requests import HTTPError
import logging
from data_collector.classes import TargetCollector
from data_collector.utils import is_IP_adress, is_host,is_url
from django.conf import settings

logger = logging.getLogger(__name__)


class Maltiverse(TargetCollector):

    BASE_URL: str = "https://api.maltiverse.com"
    maltiverse = requests.Session()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Maltiverse, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        self.init_collector()

    def init_collector(self):
        self.maltiverse.proxies = settings.PROXIES
        self.maltiverse.headers = {
            'Accept': "application/json",
            'Authorization': f"Bearer {self.secrets['api_key']}"
        }

    def make_request(self, final_url="", params=..., data=...):
        try:
            response = self.maltiverse.get(final_url)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
        return response.json()


    def ip(self,ip):
        final_url = self.BASE_URL + f"/ip/{ip}"
        return self.make_request(final_url)
        
    def host(self,host):
        final_url = self.BASE_URL + f"/host/{host}"
        return self.make_request(final_url)
    
    def url(self,url):
        final_url = self.BASE_URL + f"/url{url}"
        return self.make_request(final_url)


    def collect(self):
        pass
    
    def collect_target(self, target):
        if is_IP_adress(target):
            return self.ip(target)
        elif is_host(target):
            return self.host(target)
        elif is_url(target):
            return self.url(target)