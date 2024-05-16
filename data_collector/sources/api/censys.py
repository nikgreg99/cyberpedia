import logging
import requests

from requests import HTTPError
from data_collector.classes import TargetCollector
from data_collector.utils import ip_address
from django.conf import settings

logger = logging.getLogger()


class Censys(TargetCollector):
    """
        Wrapper for Censys API
    """
    BASE_URL = "https://search.censys.io/api/v2/search"
    censys = requests.Session()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Censys, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        self.init_collector()     

    def init_collector(self):
        self.secret = self.secrets["secret"]
        self.api_key = self.secrets["api_key"]
        self.censys.headers = {
            'Accept': 'application/json',
        }
        self.censys.proxies = settings.PROXIES

    def make_request(self, final_url=""):
        try:
            response = self.censys.get(final_url,auth=(self.secret,self.api_key))
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
        return response.json()

    def collect_target(self, target):
        if ip_address(target):
            final_url = self.BASE_URL + f"/hosts/{target}"
            return self.make_request(final_url=final_url)
