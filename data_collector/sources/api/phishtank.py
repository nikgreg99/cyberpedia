import logging 
import requests
from requests import HTTPError
from data_collector.classes import FeedCollector
from django.conf import settings

logger = logging.getLogger(__name__)


class PhishTank(FeedCollector):

    base_url: str = "https://data.phishtank.com"
    FEED_FILE_NAME = "online-valid.json"

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(PhishTank,cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        self.init_collector()

    def init_collector(self):
        self.username = self.secrets["username"]
        self.api_key = self.secrets["api_key"]
        self.phishtan = requests.Session()
        self.phishtan.headers = {
            'User-Agent': f'phishtank/{self.username}'
        }
        self.phishtan.proxies = settings.PROXIES

    def make_request(self, method="GET", final_url="", params={}, data={}):
        try:
            response = self.phishtan.get(final_url)
        except HTTPError as ex:
            logger.exception(ex)
            self.error["phishtank"] = ex
        return response.json()

    def collect_target(self):
        final_url = self.base_url + f"{self.api_key}/{self.FEED_FILE_NAME}"
        data = self.make_request(final_url)
        return data
