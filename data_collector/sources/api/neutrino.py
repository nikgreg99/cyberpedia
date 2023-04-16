import requests
from requests import HTTPError
import logging
from data_collector.classes import Collector

logger = logging.getLogger()

class Neutrino(Collector):

    base_url: str = "https://neutrinoapi.net"
    neutrino = requests.Session()

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def init_collector(self):
        self.user_id = self.secrets["user_id"]
        self.test_key = self.secrets["api_key_test"]
        self.prod_key = self.secrets["api_key_production"]
        self.headers = {
            "User-ID": self.user_id,
            "API-Key": self.test_key # just for now
        }

    def make_neutrino_request(self,final_url,data=None):
        try:
            response = self.neutrino.get(final_url,data=data,headers=self.headers)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
        return response.json()

    def email_verify(self,email):
        data = {
            "email": email,
            "fix-typos": False
        }
        final_url = self.base_url + "/email-verify"
        return self.make_neutrino_request(final_url,data)
    
    def ip_blocklist_download(self):
        final_url = self.base_url + "/ip-blocklist-download"
        data = {
            'format': 'csv',
            'cidr': True,
            'ip6': True,
            'include-vpn': False
        }
        try:
            response = self.neutrino.get(final_url,headers=self.headers,data=data)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
        return response
    
    def host_reputation(self,target):
        final_url = self.base + "/host-reputation"
        data = {'host': target}
        return self.make_neutrino_request(final_url,data)




    
    
