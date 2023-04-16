import virustotal_python
from virustotal_python.virustotal import VirustotalError
import logging
from data_collector.classes import Collector
from data_collector.utils import validate_ip_address

logger = logging.getLogger(__name__ )

class VirusTotal(Collector):

    vt_instance = None

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def init_collector(self):
        api_key = self.secrets["api_key"]
        self.vt_instance = virustotal_python.Virustotal(
            API_KEY=api_key, API_VERSION=3
        )
        self.headers = {
            "Accept": "application/json"
        }

    def scan_url(self,url):
        headers = self.headers
        headers["Content-Type"] = "application/x-www-form-urlencoded"

    def ip_address_report(self,ip):
        if validate_ip_address(ip):
            try:
                response =  self.vt_instance.request(f"/ip_address/{ip}",)
            except VirustotalError as ex:
                logger.exception(ex)
            return response.jpi
    
    def domain_report(self,ip):
        try:
            response =  self.vt_instance.request(f"/domanin/{ip}")
        except VirustotalError as ex:
            logger.exception(ex)
        return response.json()

    def collect(self): 
        pass

    def collect_target(self):
        pass