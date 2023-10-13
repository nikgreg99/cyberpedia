import virustotal_python
from virustotal_python.virustotal import VirustotalError
import logging
from data_collector.classes import TargetCollector
from data_collector.utils import validate_ip_address
from django.conf import settings

logger = logging.getLogger(__name__ )

class VirusTotal(TargetCollector):

    vt_instance = None

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        self.init_collector()

    def init_collector(self):
        api_key = self.secrets["api_key"]
        self.vt_instance = virustotal_python.Virustotal(
            API_KEY=api_key, 
            API_VERSION=3,
            PROXIES = settings.PROXIES)
        self.err = {}
        
    def ip_report(self,ip):
        try:
            response =  self.vt_instance.request(resource=f"/ip_addresses/{ip}")
        except VirustotalError as ex:
            logger.exception(ex)
            self.err['vt'] = ex
        return response.json();
    
    def domain_report(self,ip):
        try:
            response =  self.vt_instance.request(resource=f"/domain/{ip}")
        except VirustotalError as ex:
            logger.exception(ex)
            self.err['vt'] = ex
        return response.json()

    def collect(self): 
        pass

    def collect_target(self,target):
        if validate_ip_address(target):
            return self.ip_report(target)
        