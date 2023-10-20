import logging
import requests
from requests import HTTPError
from data_collector.classes import FeedCollector,TargetCollector
from django.conf import settings

logger = logging.getLogger(__name__)

class UrlHaus(FeedCollector,TargetCollector):
    base_url : str = 'https://urlhaus-api.abuse.ch/v1/'
    urlhaus = requests.Session()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(UrlHaus, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
       super().__init__(self.__class__.__name__)
       self.init_collector()


    def init_collector(self):
        self.error = {}
        self.api_key = self.secrets["api_key"]
        self.urlhaus.proxies = settings.PROXIES

    def make_request(self,final_url,params={},data={}):
        try:
            response = self.urlhaus.get(final_url,params=params,data=data)
            response.raise_for_status()
        except HTTPError as ex:
            self.error["urlhaus"] = ex
            logger.exception(ex)
        return response.json()

    def query_recent_urls(self,limit = None):
        basic_url = "urls/recent"
        query_URL = self.base_url + basic_url
        if limit is not None:
            query_URL = query_URL + f"/limit/{limit}"
        return self.make_request(final_url=query_URL)
      
    
    def query_recent_payloads(self,limit = None):
        basic_url = "payloads/recent"
        query_URL = self.base_url + basic_url
        if limit is not  None:
            query_URL = query_URL + f"/limit/{limit}"
        return self.make_request(final_url= query_URL)
    
    def collect(self):
        urls = self.query_recent_urls()
        payloads = self.query_recent_payloads()
        return {
            'url': urls,
            'payload': payloads
        }
    
    def collect_target(self, target):
        return super().collect_target(target)