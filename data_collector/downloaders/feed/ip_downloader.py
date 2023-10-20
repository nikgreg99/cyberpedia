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
        abuse = []
        hybrid_analysis = []
        sample = IPs[0:100]
        logger.log(sample)
        for ip in sample:
            remote_host = ip['remote_host']
            self.add(ip_info,self.IP_INFO,remote_host)
            self.add(abuse,self.ABUSE_IPDB,abuse)
            self.add(hybrid_analysis,self.HYBRID_ANALYSIS,hybrid_analysis)
        logger.info(ip_info)
        logger.info(abuse)
        logger.info(hybrid_analysis)
        return {
            'ipinfo': ip_info,
            'abuse': abuse,
            'hybrid-analysis': hybrid_analysis
        }
        

    def download_IP(self):
        data = sources[self.HONEY_DB].collect()
        process_data = self.process_IP(data)
        if settings.DEBUG:
            logger.info(data['bad-ip'])
            logger.info(data['twitter-ip'])
        self.elastic.insert('honeydb-bad-ip',data['bad-ip'])
        self.elastic.insert('honeydb-twitter-feed',data['twitter-ip'])
        self.elastic.insert('ip-info',process_data['ipinfo'])
        self.elastic.insert('abuseipdb',process_data['abuse'])
        self.elastic.insert('hybrid-analysis-host',process_data['hybrid-analysis'])

        

    def download_feed(self):
        self.download_IP()