import logging
import cloudmersive_validate_api_client
import cloudmersive_virus_api_client
from cloudmersive_validate_api_client.rest import ApiException
from data_collector.classes import Collector
from data_collector.utils import validate_ip_address

logger = logging.getLogger(__name__)

class Cloudmersive(Collector):

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)



    def init_collector(self):
        self.api_key = self.secrets["api_key"]
        self.config = cloudmersive_validate_api_client.Configuration()
        self.config.api_key["Apikey"] = self.api_key
       
    
    def check_ip(self,ip):
        if validate_ip_address(ip):
            cloudmersive_ip_address = cloudmersive_validate_api_client.AddressApi(self.config)
            try:
                api_response = cloudmersive_ip_address.i_p_address_ip_intelligence(ip)
            except ApiException as ex:
                logger.exception(ex)
        
            return api_response
        
    def check_domanin(self,domain):
        cloudmersive_domain = cloudmersive_validate_api_client.DomainApi(self.config)
        try:
            api_response = cloudmersive_domain.domain_check(domain)
        except ApiException as ex:
            logger.exception(ex)

        return api_response
    

    def scan_virus(self,path):
        cloudmersive_scan_virus = cloudmersive_virus_api_client.ScanApi(self.config)
        try:
            api_response = cloudmersive_scan_virus.scan_file(path)
        except ApiException as ex:
            logger.exception(ex)
        
        return api_response
    
             





    
    