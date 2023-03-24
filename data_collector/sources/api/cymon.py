import logging
import requests
from requests import HTTPError
from data_collector.classes import Collector
from data_collector.utils import validate_ip_address

logging = logging.getLogger(__name__)


class CymonInvalidAuthentication(Exception):
    pass

class Cymon(Collector):

    base_url : str = "https://api.cymon.io/v2"
    cymon = requests.Session()
   
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
            
    def init_collector(self):
        self. headers = {
          "Content Type" : "application/json",
        }
        self.auth()


    def make_cymon_request(self,final_url,data = {}):
        try:
            response = self.cymon.get(final_url,headers=self.headers,data=data)
            response.raise_for_status
        except HTTPError as ex:
            logging.error("Failing listing feeds")
        return response
    
    
    def auth(self):
         final_url = self.base_url + "/auth/login"
         username = self._secrets["username"]
         password = self._secrets["password"]
         data = {username,password}
         response = self.make_cymon_request(final_url,data)
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
        if validate_ip_address(ip):
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
    

    def get_feed_report(self,feed_id,report_id):
        pass

    def collect_target(self, target):
        return super().collect_target(target)
    
