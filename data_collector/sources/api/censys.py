from censys.search import CensysHosts
from censys.search import CensysCertificates
from data_collector.classes import TargetCollector
import logging

logger = logging.getLogger()

class Censys(TargetCollector):
    
    censys_host_client = None
    censys_certificates_client = None

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        self.init_collector()
        

    def init_collector(self):
        secret = self.secrets["secret"]
        api_key = self.secrets["api_key"]
        self.censys_host_client = CensysHosts(api_secret=secret,api_id=api_key)
        self.censys_certificates_client = CensysCertificates(api_secret=secret,api_id=api_key)

    def collect_certificates(self):
       # try:
        response =  self.censys_certificates_client.bulk()
        #except APIError as ex:
        return response


    def collect_target(self, target):
        response = self.censys_host.search(target)
        return response


    