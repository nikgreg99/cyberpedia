import requests
import logging
from requests import HTTPError
from django.conf import settings
from data_collector.classes import FeedCollector
from data_collector.helpers import csv_to_json

logger = logging.Logger(__name__)

class Maldatabase(FeedCollector):

    base_url = 'https://api.maldatabase.com'
    maldatabase = requests.Session()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Maldatabase, cls).__new__(cls)
        return cls.instance

    def __init__(self):
       super().__init__(self.__class__.__name__)
       self.init_collector()
    
    def init_collector(self):
        self.error = {}
        self.maldatabase.headers = {
            "Authorization": self.secrets["api_key"],
            "Accept-Encoding": "gzip, deflate"
        }
        self.maldatabase.proxies = settings.PROXIES

    def make_request(self, final_url, params={}, data={}):
        try:         
            response = self.maldatabase.get(final_url)
            response.raise_for_status()
        except HTTPError as ex:
            logger.error(ex)
        return response

    def collect(self):
        final_url = self.base_url + "/download"
        response = self.make_request(final_url)
        return csv_to_json(response.text)
