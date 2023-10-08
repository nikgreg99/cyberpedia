import logging
import requests
from requests import HTTPError
from data_collector.classes import TargetCollector
from data_collector.utils import validate_ip_address
from django.conf import settings

logger = logging.getLogger(__name__)

MAX_AGE_IN_DAYS = 90

class AbuseIPDB(TargetCollector):
    base_url : str = "https://api.abuseipdb.com/api/v2"
    abuseipdb = requests.Session()

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
            response = self.abuseipdb.get(final_url,params=params,headers=self.headers)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
            ex["abuseipdb"] = ex
        return response.json()

    def check_ip(self,ip):
        if validate_ip_address(ip):
            final_url = self.base_url + "/check"
            params = {
                "ipAddress": ip,
                "maxAgeInDays": MAX_AGE_IN_DAYS
            }
            return self.make_request(final_url=final_url,params=params)
        
    def collect_target(self, target):
        return self.check_ip(target)
