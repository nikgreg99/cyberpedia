import requests
from requests import HTTPError
import logging
from data_collector.classes import TargetCollector
from django.conf import settings

logger = logging.getLogger(__name__)


class DNSDB(TargetCollector):

    base_url = "https://api.dnsdb.io/v1"
    dns_db = requests.Session()

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def init_collector(self):
        api_id = self.secrets["api_id"]
        api_key = self.secrets["api_key"]
        self.dns_db.headers = {
            "API-ID": api_id,
            "API-KEY": api_key
        }
        self.dns_db.proxies = settings.PROXIES

    def collect_target(self, target):
        final_url = self.base_url + "/search"
        param = {'domain': target}
        try:
            response = self.dns_db.get(final_url,headers=self.headers,params=param)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
        return response.json()