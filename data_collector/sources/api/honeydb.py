import logging
import requests
from requests import HTTPError
from data_collector.classes import Collector
from django.conf import settings

logger = logging.getLogger(__name__)

class HoneyDB(Collector):

    base_url :str = "https://honeydb.io/api"
    honeydb = requests.Session()

    def __init__(self):
       super().__init__(self.__class__.__name__)

    def init_collector(self):
        self.honey_db_api_id = self.secrets["api_id"]
        self.honey_db_api_key = self.secrets["api_key"]        
        self.honeydb.headers = {
            "X-HoneyDb-ApiId": self.honey_db_api_id,
            "X-HoneyDb-ApiKey": self.honey_db_api_key
        }
        self.honeydb.proxies = settings.PROXIES

        
    def collect_bad_ip(self):
        try:
            final_url = self.base_url + "/bad-hosts"
            response = self.honeydb.get(final_url,headers=self.honeydb.headers)
        except HTTPError as ex:
            logger.exception("Error requesting bad ip")
        
        return response.json()
    
    def collect_twitter_feed(self):
        try:
            final_url = self.base_url + "/twitter-threat-feed"
            response = self.honeydb.get(final_url,headers=self.honeydb.headers)
        except HTTPError as ex:
            pass
        return response.json()
    
    def _ip_info(self,ip):
        try:
            internet_scanner_url = self.base_url.join("/internet-scanner/info/{}".format(ip))
            response_ip_info_scanner = self.honeydb.get(internet_scanner_url,headers=self.honeydb.headers)
            ip_info = response_ip_info_scanner.json()
            ip_url = self.base_url.join("/ipinfo/{}".format(ip))
            response_ip_url = self.honeydb.get(ip_url,self.honeydb.headers)
            ip_url = response_ip_url.json()
            ip_info.extend(ip_url)
        except HTTPError as ex:
            pass
        return ip_info
    
    def collect(self):
        return super().collect()
    
    def collect_target(self, target):
        return super().collect_target(target)