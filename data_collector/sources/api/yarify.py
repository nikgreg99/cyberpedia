import logging
import requests
from requests import HTTPError
from django.conf import settings
from data_collector.classes import FeedCollector
from django.conf import settings

logger = logging.getLogger(__name__)

class Yarify(FeedCollector):

    base_url : str = "https://yaraify-api.abuse.ch/api/v1/"
    download_url : str = "https://yaraify-api.abuse.ch/download/"
    yarify =  requests.Session()

    def __init__(self):
       super().__init__(self.__class__.__name__)
       self.init_collector()

    def init_collector(self):
        self.error = {}
        self.yarify.proxies = settings.PROXIES


    def collect_recent_rules(self):
        data = {"query" : "recent_yararules"}
        try:
             response  = self.yarify.post(url= self.base_url,json=data)
             response.raise_for_status()
        except HTTPError as ex:
             self.error['yaraify'] = ex
             logging.exception(ex)
        return response.json()

     
    def collect(self):
        rules = self.collect_recent_rules()
        return rules


