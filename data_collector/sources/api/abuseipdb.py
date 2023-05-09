import logging
import requests
from requests import HTTPError
from data_collector.classes import Collector
from data_collector.utils import validate_ip_address
from django.conf import settings

logger = logging.getLogger(__name__)

MAX_AGE_IN_DAYS = 90

class AbuseIPDB(Collector):

    base_url : str = "https://api.abuseipdb.com/api/v2"
    abuseipdb = requests.Session()

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def init_collector(self):
        self.headers = {
            "Accept": 'application/json',
            "Key": self.secrets["api_key"],
        }
        self.abuseipdb.proxies = settings.PROXIES

    def request(self,final_url,params):
        try:
            response = self.abuseipdb.get(final_url,params=params,headers=self.headers)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
        return response.json()

    def check_ip(self,ip):
        if validate_ip_address(ip):
            final_url = self.base_url + "/check"
            parameters = {
                "ipAddress": ip,
                "maxAgeInDays": MAX_AGE_IN_DAYS
            }
            return self.request_abuse_ipdb(final_url,parameters)
        
    def collect_target(self, target):
        return self.check_ip(target)
