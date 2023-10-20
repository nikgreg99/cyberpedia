import logging
import requests
from requests import HTTPError
from data_collector.classes import TargetCollector
from data_collector.utils import is_ip
from django.conf import settings

logging = logging.getLogger(__name__)


class CymonInvalidAuthentication(Exception):
    pass

class Cymon(TargetCollector):

    base_url : str = "https://api.cymon.io/v2"
    cymon = requests.Session()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Cymon, cls).__new__(cls)
        return cls.instance
   
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        self.init_collector()
            
    def init_collector(self):
        self. headers = {
          "Content-Type" : "application/json",
        }
        self.cymon.proxies = settings.PROXIES
        # self.auth()


    def make_cymon_request(self,final_url,data = {}):
        try:
            response = self.cymon.get(final_url,headers=self.headers,data=data)
            response.raise_for_status()
        except HTTPError as ex:
            logging.exception(ex)
        return response
    
    
    def auth(self):
         final_url = self.base_url + "/auth/login"
         username = self.secrets["username"]
         password = self.secrets["password"]
         data = {
             "username": username,
             "password": password
        }
         response = self.cymon.post(final_url,headers=self.headers,data=data)
         if "jwt" in response.json(): 
             jwt = response.json()["jwt"]
             self.headers.update({"Authorization": "Bearer ".format(jwt)})
         else:
            raise CymonInvalidAuthentication
            

    def _list_feeds(self):
        final_url = self.base_url + "/feeds/me"
        response = self.make_cymon_request(final_url)
        list_feed = response.json()["feeds"]
        feeds_id  = []
        for feed in list_feed:
            feeds_id.append(feed["id"])
        
        return feeds_id
    
    def searcy_by_IP(self,ip):
        if is_ip(ip):
            final_url = self.base_url + "/ioc/search/ip/{}".format(ip)
            response = self.make_cymon_request(final_url)
            return response.json()
        
    def search_by_domain(self,domain):
        final_url = self.base_url + "/ioc/search/domain/{}".format(domain)
        response = self.make_cymon_request(final_url)
        return response.json()

    def search_by_hostname(self,host):
        final_url = self.base_url + "/ioc/search/hostname/{}".format(host)
        response = self.make_cymon_request(final_url)
        return response.json()

    def search_by_MD5(self,md5):
        final_url = self.base_url + "/ioc/search/md5/{}".format(md5)
        response = self.make_cymon_request(final_url)
        return response.json()

    def search_by_SHA1(self,sha1):
        final_url = self.base_url + "/ioc/search/sha1/{}".format(sha1)
        response = self.make_cymon_request(final_url)
        return response.json()
    
    def search_by_SHA256(self,sha256):
        final_url = self.base_url + "ioc/search/sha256/{}".format(sha256)
        response = self.make_cymon_request(final_url)
        return response.json()
    

    def collect_target(self, target):
        return super().collect_target(target)
    
