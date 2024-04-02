import virustotal_python
import logging
from enum import Enum
from virustotal_python.virustotal import VirustotalError
from data_collector.classes import FeedCollector, TargetCollector
from data_collector.utils import is_IP_adress,is_domain, is_url
from django.conf import settings

logger = logging.getLogger(__name__ )

class VirusTotalFeedType(Enum):
    YARA_RULES = "Yara Rules"

#STATUS: OK
class VirusTotal(FeedCollector,TargetCollector):

    vt_instance = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(VirusTotal, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)
        self.init_collector()

    def init_collector(self):
        api_key = self.secrets["api_key"]

        headers = {
            'accept': "application/json",
            "x-apikey": self.secrets["api_key"]
        }

        self.vt_instance = virustotal_python.Virustotal(
            API_KEY=api_key, 
            API_VERSION=3,
            PROXIES = settings.PROXIES
        )

        self.vt_instance.HEADERS = headers
        self.err = {}

    def submit_url(url):
        pass
    
    #According to the specification: 4 requests in 60 seconds
    def make_request(self,partial_url,method="GET"):
        try:
            response =  self.vt_instance.request(resource=partial_url,method=method)
            return response.json()
        except VirustotalError as ex:
            logger.exception(ex)
            self.err['vt'] = ex
        
    
    def collect(self,collector: VirusTotalFeedType) -> dict:
        partial_url = None
        if collector == VirusTotalFeedType.YARA_RULES:
            partial_url =  "yara_rules"

        return  self.make_request(partial_url)
    

    def collect_target(self,target):
        partial_url = None
        if is_IP_adress(target):
            partial_url = f"ip_addresses/{target}"
        else:
            partial_url = f"domains/{target}"
        
        if settings.DEBUG:
            logger.info(partial_url)

        return self.make_request(partial_url=partial_url)

        