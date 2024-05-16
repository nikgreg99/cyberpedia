import requests
from requests import HTTPError
import logging
from data_collector.classes import FeedCollector
from django.conf import settings

logger = logging.getLogger(__name__)


class FeodoTracker(FeedCollector):

    BASE_URL = "http://feodotracker.abuse.ch"
    feodo = requests.Session()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(FeodoTracker, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        self.init_collector()
            
    def init_collector(self):
        self.err = {}
        self.feodo.headers = {
            "Content-Type": "application/json",
        }
        self.feodo.proxies = settings.PROXIES

    def make_request(self, final_url="", params={},data={}):
        try:
            response = self.feodo.get(final_url, params=params)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
        return response.json()

    def collect(self) -> dict:
        ipblocklist_url = self.BASE_URL + "/downloads/ipblocklist_recommended.json"
        ipblocklist_ioc = self.BASE_URL + "/downloads/ipblocklist.json"
        return {
            'ip_blocklisted': self.make_request(ipblocklist_url),
            'ip_blocklisted_ioc': self.make_request(ipblocklist_ioc)
        }