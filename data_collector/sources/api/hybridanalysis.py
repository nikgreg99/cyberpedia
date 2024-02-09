import requests
from requests import HTTPError
import logging
from data_collector.classes import TargetCollector
from data_collector.exceptions import UnsupportedTarget
from data_collector.utils import is_domain, validate_hash, is_url, is_IP_adress
from django.conf import settings

logger = logging.getLogger(__name__)


class HybridAnalysis(TargetCollector):

    base_url: str = "https://www.hybrid-analysis.com"
    api_url: str = f"{base_url}/api/v2"
    hybrid_analysis = requests.Session()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(HybridAnalysis, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        self.init_collector()

    def init_collector(self):
        api_key = self.secrets["api_key"]
        self.hybrid_analysis.headers = {
            'api-key': api_key,
            'user-agent': 'Falcon Sandbox',
            'accept': 'application/json'
        }
        self.hybrid_analysis.proxies = settings.PROXIES
        self.error = {}

    def collect_target(self, target):

        if is_IP_adress(target):
            data = {"host": target}
            uri = "/search/terms"
        elif is_domain(target):
            data = {'domain': target}
            uri = "/search/terms"
        elif is_url(target):
            data = {"url": target}
            uri = "/search/terms"
        else:
            raise UnsupportedTarget("f{target} is non supported")

        try:
            final_url = self.api_url + uri
            respose = self.hybrid_analysis.post(final_url, data=data)
            respose.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
            self.error['vt'] = ex
        return respose.json()
