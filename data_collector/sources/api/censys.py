from censys.search import CensysHosts
from censys.search import CensysCertificates
from data_collector.classes import Collector
import logging

logger = logging.getLogger()

class Censys(Collector):
    
    censys_host_client = None
    censys_certificates_client = None

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        

    def init_collector(self):
        secret = self.secrets["secret"]
        api_key = self.secrets["api_key"]
        self.censys_host_client = CensysHosts(api_secret=secret,api_id=api_key)
        self.censys_certificates_client = CensysCertificates(api_secret=secret,api_id=api_key)

    def collect_certificates(self):
        return self.censys_certificates_client.bulk()


    def collect_target(self, target):
        return self.censys_host.search(target)


    