import requests
from requests import HTTPError
import logging
from data_collector.classes import Collector
from data_collector.exceptions import UnsupportedTarget
from data_collector.utils import validate_domain,validate_hash,validate_url,validate_ip_address

logger = logging.getLogger(__name__)

class HybridAnalysis(Collector):

    base_url : str = "https://www.hybrid-analysis.com"
    api_url : str = f"{base_url}/api/v2"
    hybrid_analysis = requests.Session()

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def init_collector(self):
        api_key = self.secrets["api_key"]
        self.hybrid_analysis.headers = {
            'api-key': api_key,
            'user-agent': 'Falcon Sandbox',
            'accept': 'application/json'
        }

    def collect_target(self, target):
        if validate_domain(target):
            data = {'domain': target}
            uri = "/search/terms"
        elif validate_hash(target):
            data = {'hash': target}
            uri = "/search/hash"
        elif validate_ip_address(target):
            data = {"host": target}
            uri = "/search/terms"
        elif validate_url(target):
            data = {"url" : target}
            uri = "/search/terms"
        else:
            raise UnsupportedTarget("f{target} is non supported")

        try:
            final_url = self.api_url + uri
            respose = self.hybrid_analysis.get(final_url,data=data)
            respose.raise_for_status()
        except HTTPError as ex:
                logger.exception(ex)
        return respose.json()
