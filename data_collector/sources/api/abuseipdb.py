import logging
import requests
from requests import HTTPError
from data_collector.classes import TargetCollector
from data_collector.exceptions import UnsupportedTarget
from data_collector.utils import is_IP_adress
from django.conf import settings

logger = logging.getLogger(__name__)



# STATUS: OK
class AbuseIPDB(TargetCollector):

    MAX_AGE_IN_DAYS = 90
    base_url: str = "https://api.abuseipdb.com/api/v2"
    abuseipdb = requests.Session()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(AbuseIPDB, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        self.init_collector()

    def init_collector(self):
        self.error = {}
        self.abuseipdb.headers = {
            "Accept": 'application/json',
            "Key": self.secrets["api_key"],
        }
        self.abuseipdb.proxies = settings.PROXIES

    def make_request(self, final_url="", params={}, data={}):
        try:
            response = self.abuseipdb.get(
                final_url, params=params, headers=self.abuseipdb.headers)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
            self.error["abuseipdb"] = ex
        return response.json()

     
    def collect_target(self, target):
        if is_IP_adress(target):
            final_url = self.base_url + "/check"
            params = {
                "ipAddress": target,
                "maxAgeInDays": self.MAX_AGE_IN_DAYS
            }
            return self.make_request(final_url=final_url, params=params)
        else:
            raise UnsupportedTarget('Target is nont valid to be analzyed')

