import logging
import requests
from requests import HTTPError
from data_collector.classes import Collector

logger = logging.getLogger(__name__)

class CVEData(Collector):
    base_url : str = "https://v1.cveapi.com"
    cve_data = requests.Session()

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def init_collector(self):
        pass
    
    def collect(self):
        raise NotImplementedError()

    def collect_target(self,target):
        final_url = self.base_url + "/{}".format(target)
        try:
            response = self.cve_data.get(final_url)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception("Error requsting CVE data")
        return response.json()
    