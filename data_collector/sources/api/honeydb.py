import logging
import requests
from requests import HTTPError
from data_collector.classes import FeedCollector,TargetCollector
from django.conf import settings

logger = logging.getLogger(__name__)

class HoneyDB(FeedCollector,TargetCollector):

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

    def make_request(self,final_url):
        try:
            response = self.honeydb.get(final_url,headers=self.honeydb.headers)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
        return response.json()

        
    def collect_bad_ip(self):
        final_url = self.base_url + "/bad-hosts"
        return self.make_request(final_url)

    
    def collect_twitter_feed(self):
        final_url = self.base_url + "/twitter-threat-feed"
        return self.make_request(final_url)
    
    def collect_services(self):
        final_url = self.base_url + "/services"
        return self.make_request(final_url)
    
    def stats_asn(self):
        final_url = self.base_url + "/stats/asn"
        return self.make_request(final_url)

    def internet_scanner_info(self,target):
        final_url = self.base_url + f"/internet-scanner/info/{target}"
        return self.make_request(final_url)
    
    def ip_info(self,target):
        final_url = self.base_url + f"/ip-info/bogon{target}"
        return self.make_request(final_url)

    def collect(self):
        return self.collect_bad_ip(),self.collect_twitter_feed()
    
    
    def collect_target(self, target):
        return self.internet_scanner_info(target),self.ip_info(target)