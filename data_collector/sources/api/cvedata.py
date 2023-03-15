import logging
import requests
from requests import HTTPError
from data_collector.classes import Collector

logger = logging.getLogger(__name__)

class CVEData(Collector):
    base_url : str = "https://v1.cveapi.com"
    cve_data = requests.Session()

    def collect_target(self,target):
        final_url = self.base_url + "/{}".format(target)
        try:
            response = self.cve_data.get(final_url)
            response.raise_for_status()
        except HTTPError as ex:
            logger.exception("Error requsting CVE data")
        return response.json()
    