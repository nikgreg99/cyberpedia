import logging
import requests
from requests import HTTPError
from data_collector.classes import FeedCollector
from django.conf import settings

logger = logging.getLogger(__name__)


class HoneyDB(FeedCollector):

    base_url: str = "https://honeydb.io/api"
    honeydb = requests.Session()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(HoneyDB, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        super().__init__(self.__class__.__name__)
        self.init_collector()

    def init_collector(self):
        self.honey_db_api_id = self.secrets["api_id"]
        self.honey_db_api_key = self.secrets["api_key"]
        
        self.honeydb.headers = {
            "X-HoneyDb-ApiId": self.honey_db_api_id,
            "X-HoneyDb-ApiKey": self.honey_db_api_key
        }
        self.error = {}
        self.honeydb.proxies = settings.PROXIES

    def make_request(self, final_url):
        try:
            response = self.honeydb.get(
                final_url, headers=self.honeydb.headers)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
            self.error['honeydb'] = ex
        return response.json()

    def collect_bad_ip(self):
        final_url = self.base_url + "/bad-hosts"
        return self.make_request(final_url)

    def collect_twitter_feed(self):
        final_url = self.base_url + "/twitter-threat-feed"
        return self.make_request(final_url)

    def collect_asn(self):
        final_url = self.base_url + "/stats/asn"
        return self.make_request(final_url)

    def collect(self):
        bad_ip = self.collect_bad_ip()
        twitter_ip = self.collect_twitter_feed()
        return {
            'bad-ip': bad_ip,
            'twitter-ip': twitter_ip
        }
