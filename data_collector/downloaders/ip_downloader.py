import logging
from .downloader import DataDownloader
from data_collector.sources.apps import sources

logger = logging.getLogger(__name__)

SHODAN = 'Shodan'
IP_INFO = 'IPInfo'
ABUSE_IPDB = 'AbuseIPDB'
HYBRID_ANALYSIS = 'HybridAnalysis'
MALTIVERSE = 'Maltiverse'


class IPDownloader(DataDownloader):

    _self = None
    HONEY_DB = 'HoneyDB'

    @classmethod
    def init(cls):
        if cls._self is None:
            cls._self = super().__init__(cls)
        return cls._self
    
    def __init__(self) -> None:
        super().__init__()
    
    def add(self,list,key,ip):
        result = sources[key].collect_target(ip)
        list.append(result)
    
    def process_IP(self,IPs):
        shodan =  []
        ip_info = []
        abuse_ipdb = []
        hb_ip = []
        maltiverse = []
        for ip in IPs:
            remote_host = ip['remote_host']
            self.add(shodan,SHODAN,remote_host)
            self.add(ip_info,IP_INFO,remote_host)
            self.add(abuse_ipdb,ABUSE_IPDB,remote_host)
            self.add(hb_ip,HYBRID_ANALYSIS,remote_host)
            self.add(maltiverse,MALTIVERSE,remote_host)

    def download_IP(self):
        bad_id, twitter_feed = sources[self.HONEY_DB].collect()
        self.process_IP(bad_id)
        self.process_IP(twitter_feed)
        

    def download_data(self):
        self.download_IP()