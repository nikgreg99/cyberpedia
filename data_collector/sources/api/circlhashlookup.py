import requests
from requests import HTTPError
from data_collector.classes import TargetCollector
from django.conf import settings
import logging


logger = logging.getLogger(__name__)

class CIRCLHashLookup(TargetCollector):

    base_url : str = "https://hashlookup.circl.lu"
    circl_hash_lookup = requests.Session()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(CIRCLHashLookup, cls).__new__(cls)
        return cls.instance

    def __init__(self, name) -> None:
        super().__init__(self.__class__.__name__)
        self.init_collector()

    def init_collector(self):
        self.circl_hash_lookup.proxies = settings.PROXIES
        self.circl_hash_lookup.headers = {
            'Accept': 'application/json'
        }

    def make_request(self,final_url,params={},data={}):
        try:
            response = self.circl_hash_lookup.get(final_url,params=params,data=data)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
        return response.json()


    def lookup_md5(self,md5 : str):
        final_url = self.base_url + f"/lookup/md5/{md5}"
        return self.make_request(final_url)

    def lookuo_SHA1(self, sha1: str):
        final_url = self.base_url  + f"/lookup/sha1/{sha1}"
        return self.make_request(final_url)
    
    def lookuo_SHA256(self,sha256: str):
        final_url = self.base_url + f"/lookup/sha256/{sha256}"
        return self.make_request(final_url)
    
    def collect_target(self) -> dict:
        return super().collect_target()
