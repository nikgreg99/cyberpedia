import logging
import requests
from requests import HTTPError
from data_collector.classes import Collector

logger = logging.getLogger(__name__)

class UrlHaus(Collector):
    base_url : str = 'https://urlhaus-api.abuse.ch/v1/'
    api_key = None
    urlhaus = requests.Session()


    def _init_(self):
        pass

    def _make_request(self,url):
        try:
            response = self.urlhaus.get(url)
            response.raise_for_status()
        except HTTPError as ex:
            pass
        return response.json()

    def query_recent_URL(self,limit = None):
        basic_url = "urls/recent"
        query_URL = self.base_url + basic_url
        if limit is not None:
            query_URL = query_URL + "/limit/{}".format(limit)
        return self._make_request(query_URL)
      
    
    def query_recent_payloads(self,limit = None):
        basic_url = "payloads/recent"
        query_URL = self.base_url + basic_url
        if limit is not  None:
            query_URL = query_URL + "/limit/{}".format(limit)
        return self._make_request(query_URL)