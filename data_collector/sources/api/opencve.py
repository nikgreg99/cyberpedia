import requests
from requests import HTTPError
import logging
from data_collector.classes import Collector

logger = logging.getLogger(__name__)


class OpenCVE(Collector):

    base_url : str = "https://www.opencve.io/api"
    open_cve = requests.Session()

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def init_collector(self):
        username = self.secrets["username"]
        password = self.secrets["password"]
        self.headers = {
            "Authorization": "{}:{}".format(username,password),
            "Accept": "application/json"
        }

    def make_requets_open_cve(self,final_url):
        try:
            response = self.open_cve.get(final_url,headers = self.headers)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception(ex)
        return response.json()
    
    def list_CVE(self):
        final_url = self.base_url + "/cve"
        return self.make_requets_open_cve(final_url)
    
    def list_CWE(self):
        final_url = self.base_url + "/cwe"
        return self.make_requets_open_cve(final_url)
    
    def collect_target(self, target):
        return super().collect_target(target)
    
    def collect(self):
        return super().collect()