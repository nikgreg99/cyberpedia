import requests
from requests import HTTPError
import logging
from data_collector.classes import TargetCollector
from data_collector.exceptions import UnsupportedTarget
from data_collector.utils import validate_domain,validate_hash,validate_url,validate_ip_address
from django.conf import settings

logger = logging.getLogger(__name__)

class HybridAnalysis(TargetCollector):

    base_url : str = "https://www.hybrid-analysis.com"
    api_url : str = f"{base_url}/api/v2"
    hybrid_analysis = requests.Session()

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
        
        if validate_ip_address(target):
            data = {"host": target}
            uri = "/search/terms"
        elif validate_domain(target):
            data = {'domain': target}
            uri = "/search/terms"
        elif validate_url(target):
            data = {"url" : target}
            uri = "/search/terms"
        else:
            raise UnsupportedTarget("f{target} is non supported")

        try:
            final_url = self.api_url + uri
            respose = self.hybrid_analysis.post(final_url,data=data)
            respose.raise_for_status()
        except HTTPError as ex:
                logger.exception(ex)
                self.error['vt'] = ex
        return respose.json()
