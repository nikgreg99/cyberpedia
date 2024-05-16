import requests
from requests import HTTPError

from data_collector.helpers import get_hash_type
from data_collector.classes import TargetCollector
from django.conf import settings
import logging


logger = logging.getLogger(__name__)


class CIRCLHashLookup(TargetCollector):

    BASE_URL : str = "https://hashlookup.circl.lu/"
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

    def lookup_md5(self, md5: str):
        final_url = self.BASE_URL + f"lookup/md5/{md5}"
        return self.make_request(final_url)

    def lookup_SHA1(self, sha1: str):
        final_url = self.BASE_URL  + f"lookup/sha1/{sha1}"
        return self.make_request(final_url)
    
    def lookup_SHA256(self,sha256: str):
        final_url = self.BASE_URL + f"lookup/sha256/{sha256}"
        return self.make_request(final_url)
    
    def collect_target(self,observable) -> dict:
        
        hash_type = get_hash_type()
        response = None

        if hash_type == "md5":
            response = self.lookup_md5(observable)
        elif hash_type == "sha1":
            response =  self.lookup_SHA1(observable)
        elif hash_type == "sha256"
            response = self.lookup_SHA256(observable)
        
        return response

