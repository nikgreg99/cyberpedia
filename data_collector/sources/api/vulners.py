import vulners
from vulners.base import VulnersApiError
import logging
from data_collector.classes import Collector
from django.conf import settings

logger = logging.getLogger(__name__)

class Vulners(Collector):

    base_url : str = "https://vulners.com/api/v3"

    def __init__(self) -> None:
       super().__init__(self.__class__.__name__)

    def init_collector(self):
        self.api_key = self.secrets["api_key"]
        self.vulners = vulners.VulnersApi(api_key = self.api_key, proxies = settings.PROXIES)
        


    def search_target(self,target):
        try:
            response = self.vulners.find_all(target, limit=1000, fields=['*'])
        except VulnersApiError as ex:
            logger.exception(ex)
        return response

    def CVE_by_id(self,CVE):
        try:
            CVE_response = self.vulners.get_bulletin(CVE, fields=["*"])
        except VulnersApiError as ex:
            logger.exception(ex)
        return CVE_response
    
    def CVE_references(self,CVE):
        try:
            cve_references = self.vulners.get_bulletin_references(cve_references)
        except VulnersApiError as ex:
            logger.error(ex)
        return cve_references
    
    def CVEs_by_ids(self,CVEs: list):
        try:
            CVE_responses = self.vulners.get_bulletins(CVEs, fields=["*"])
        except VulnersApiError as ex:
             logger.error(ex)
        return CVE_responses
    
    def vulnerabilities_by_CPE(self,CPE):
        try:
            cpe_results = self.vulners_api.cpeVulnerabilities(CPE)
            cpe_exploit_list = cpe_results.get('exploit')
            cpe_vulnerabilities_list = [cpe_results.get(key) for key in cpe_results if key not in ['info', 'blog', 'bugbounty']]
        except VulnersApiError as ex:
             logger.error(ex)
        return cpe_exploit_list,cpe_vulnerabilities_list
    
    def collect(self):
        try:
            all_cve = self.vulners.get_collection("cve")
        except ValueError as ex:
             logger.error(ex)
        return all_cve
    
    def collect_target(self, target):
        pass