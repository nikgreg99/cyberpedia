import logging
import requests
from requests import HTTPError
from data_collector.classes import FeedCollector
from django.conf import settings

logger = logging.getLogger(__name__)


class Yarify(FeedCollector):

    BASE_URL: str = "https://yaraify-api.abuse.ch/api/v1/"
    DOWNLOAD_URL: str = "https://yaraify-api.abuse.ch/download/"
    yarify = requests.Session()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Yarify, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        super().__init__(self.__class__.__name__)
        self.init_collector()

    def init_collector(self):
        self.yarify.headers = {
            'Accept': "application/json"
        }
        self.yarify.proxies = settings.PROXIES

    def collect_recent_rules(self):
        data = {"query": "recent_yararules"}
        try:
            response = self.yarify.post(url= self.BASE_URL,json=data)
            response.raise_for_status()
        except HTTPError as ex:
            logging.exception(ex)
        return response.json()
 
    def collect(self):
        rules = self.collect_recent_rules()
        return rules['data']
