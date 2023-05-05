import requests
from requests import HTTPError
from data_collector.classes import Collector
from django.conf import settings
import logging


logger = logging.getLogger(__name__)

class CIRCLHashLookup(Collector):

    base_url : str = "https://hashlookup.circl.lu"
    circl_hash_lookup = requests.Session()

    def __init__(self, name) -> None:
        super().__init__(self.__class__.__name__)

    def init_collector(self):
        self.circl_hash_lookup.proxies = settings.PROXIES
        self.circl_hash_lookup.headers = {
            'Accept': 'application/json'
        }

    def make_request(self,final_url,headers=None,data=None):
        try:
            response = self.circl_hash_lookup.get(final_url,headers=headers,data=data)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
        return response.json()


    def bulk_md5(self,hashesh: list):
        data= {'hashes': hashesh}
        final_url = self.base_url + "/bulk/md5"
        return self.make_request(final_url,data=data)

    def bulk_SHA1(self,hashes):
        data = {'hashesh:', hashes}
        final_url = self.base_url  + "/bulk/sha1"
        return self.make_request(final_url,data=data)
