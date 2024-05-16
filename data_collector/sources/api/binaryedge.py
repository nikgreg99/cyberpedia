import logging
import requests

from requests import HTTPError
from data_collector.classes import TargetCollector
from data_collector.helpers import is_ip_address, is_url_or_domain
from django.conf import settings

logger = logging.getLogger(__name__)


class BinaryEdge(TargetCollector):

    BASE_URL = "https://api.binaryedge.io/v2/query/"
    binary_edge = requests.Session()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(BinaryEdge, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        self.init_collector()
   
    def init_collector(self):
        self.binary_edge.headers = {
            'X-Key': self.secrets["api-key"]
        }
        self.binary_edge.proxies = settings.PROXIES

    def make_get_request(self, final_url="", params={} data={}):
        try:
            response = self.binary_edge.get(final_url)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
        return response

    def collect_target(self,target) -> dict:
        results = None
        if is_ip_address(target):
            url_recent_ip_info = self.BASE_URL + f"ip/{target}"
            resp_ip_info = self.make_get_request(url_recent_ip_info)

            url_query_ip = self.BASE_URL + f"search/?query=ip:{target}"
            resp_query_ip = self.make_get_request(url_query_ip)

            results = {
                "ip_recent_report": resp_ip_info.json(),
                "ip_query_report": resp_query_ip.json()
            }

        elif is_url_or_domain() == "domain":
            url_domain_report = self.BASE_URL + f"/domains/subdomain/{target}"
            resp_domain_report = self.make_get_request(url_domain_report)
            results = resp_domain_report.json()

        return results