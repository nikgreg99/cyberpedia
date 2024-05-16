import logging
import requests


from requests import HTTPError
from data_collector.classes import TargetCollector
from data_collector.helpers import is_ip_address
from django.conf import settings

logger = logging.getLogger(__name__)


class ZoomEye(TargetCollector):

    BASE_URL: str = "https://api.zoomeye.org/"
    zoomeye = requests.Session()

    search_type: str
    query: str
    page: str
    facets: str
    history: bool

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        self.init_collector()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ZoomEye, cls).__new__(cls)
        return cls.instance

    def init_collector(self):
        api_key = self.secrets["api_key"]
        self.zoomeye.headers = {
            "API-KEY": {api_key}
        }

        self.zoomeye.proxies = settings.PROXIES

    def create_zoomeye_url(self,target):
        if is_ip_address(target):
            self.query += f" ip:{target}"
        else:
            self.query += f" host:{target}"
            self.search_type = "host"

        if self.search_type in ["host", "web"]:
            final_url = self.BASE_URL + self.search_type + "/search?query="
            final_url += self.query

            if self.page:
                final_url += f"&page={self.page}"

            if self.facets:
                final_url += f"&facet={','.join(self.facets)}"

        elif self.search_type == "both":
            final_url = self.BASE_URL + "both/search?"
            if self.history:
                final_url = f"history={self.history}&"
            final_url += f"ip={target}"
        else:
            raise Exception

    def make_request(self, final_url="", params={}):
        try:
            response = self.zoomeye.get(final_url,params=params)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
            self.error['zoomeye'] = ex
        return response.json()

    def collect_target(self, target):
        final_url = self.create_zoomeye_url(target)
        response = self.make_request(final_url)

        result = {"request_options": {}}
        result["request_options"]["search_type"] = self.search_type
        result["request_options"]["query"] = self.query

        if self.page:
            result["request_options"]["page"] = self.page
        if self.facets:
            result["request_options"]["facets"] = self.facets
        if self.history and self.search_type == "both":
            result["request_options"]["history"] = self.history

        result.update(response.json())

        return result
