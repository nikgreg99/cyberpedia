import logging
import requests
from requests import HTTPError
from data_collector.classes import TargetCollector
from data_collector.utils import validate_cve_format
from django.conf import settings

logger = logging.getLogger(__name__)

class CVEData(TargetCollector):
    _self = None
    base_url : str = "https://v1.cveapi.com"
    cve_data = requests.Session()

    @classmethod
    def init(cls):
        if cls._self is None:
            cls._self = super().__init__(cls)
        return cls._self

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        self.init_collector()

    def init_collector(self):
        self.error = {}
        self.cve_data.proxies = settings.PROXIES
    
    def make_request(self,final_url,params={}, data={}):
        try:
            response = self.cve_data.get(final_url)
            response.raise_for_status()
        except HTTPError as ex:
                logger.exception(ex)
                self.error['cvedata'] = ex
        return response.json()

    def collect_target(self,target):
        if validate_cve_format(target):
            final_url = self.base_url + f"/{target}"
            data = self.make_request(final_url)
        return data

    