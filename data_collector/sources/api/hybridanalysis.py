import requests
from requests import HTTPError
import logging
from ratelimit import limits
from data_collector.classes import TargetCollector,FeedCollector
from data_collector.utils import is_domain, is_IP_adress
from django.conf import settings

logger = logging.getLogger(__name__)


# STATUS: OK
class HybridAnalysis(FeedCollector,TargetCollector):

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

    @limits(calls=200,period=60)
    def make_get_request(self, final_url="", params={}, data={}):
        try:
            response = self.hybrid_analysis.get(final_url)
            response.raise_for_status()
        except HTTPError as ex:
            self.error['hybridanalysis'] = ex
        
        return response.json()

    def collect(self) -> dict:
        final_url = self.api_url + "/feed/latest"
        response = self.make_get_request(final_url=final_url)
        return response['data']

    def collect_target(self, target):

        if is_IP_adress(target):
            data = {"host": target}
            ending_url = "/search/terms"
        elif is_domain(target):
            data = {'domain': target}
            ending_url = "/search/terms"
        else:
            data = {"url": target}
            ending_url = "/search/terms"

        try:
            final_url = self.api_url + ending_url
            respose = self.hybrid_analysis.post(final_url, data=data)
            respose.raise_for_status()
        except HTTPError as ex:
            self.error['hybrid-analysis'] = ex
        return respose
