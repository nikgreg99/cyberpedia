import logging
from .feed_downloader import FeedDownloader
from data_collector.apps import sources
from django.conf import settings



logger = logging.getLogger(__name__)


class IPDownloader(FeedDownloader):

    _self = None
    HONEY_DB = 'HoneyDB'
    SHODAN = 'Shodan'
    IP_INFO = 'IPInfo'
    ABUSE_IPDB = 'AbuseIPDB'
    HYBRID_ANALYSIS = 'HybridAnalysis'
    WHOIS = 'Whois'

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
        ip_info = []
       
        for ip in IPs:
            remote_host = ip['remote_host']
            self.add(ip_info,self.IP_INFO,remote_host)
        return ip_info,
        

    def download_IP(self):
        data = sources[self.HONEY_DB].collect()
        if settings.DEBUG:
            logger.info(data['bad-ip'])
            logger.info(data['twitter-ip'])
        self.elastic.insert('honeydb-bad-ip',data['bad-ip'])
        self.elastic.insert('honeydb-twitter-feed',data['twitter-ip'])
        

    def download_feed(self):
        self.download_IP()