import requests
from requests import HTTPError
import logging
from data_collector.utils import validate_ip_address
from data_collector.classes import Collector
from django.conf import settings

logger = logging.getLogger(__name__)


class AbuseIPDB(Collector):

    base_url : str = "https://api.abuseipdb.com/api/v2"
    abuseipdbb = requests.Session()

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def init_collector(self):
        self.headers = {
            "Accept": 'application/json',
            "Key": self.secrets["api_key"]
        }
        self.abuseipdbb.proxies = {settings.PROXIES}

    def request_abuse_ipdb(self,final_url,params):
        try:
            response = self.abuseipdbb.get(final_url,params=params)
            response.raise_for_status()
        except HTTPError as ex:
            logger.ex(ex)
        return response.json()

    def check_ip(self,ip):
        if validate_ip_address(ip):
            final_url = self.base_url + "/check"
            parameters = {
                "ipAddress": ip
            }
            return self.request_abuse_ipdb(final_url,parameters)
