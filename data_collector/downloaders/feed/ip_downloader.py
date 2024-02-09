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
    
    def process_IP(self,IP):
        ipinfo = []
        abuse = []
        hybrid_analysis = []
        shodan = []
        greynoise = []
        ipapi = []
        ipapicom = []
        maltiverse = []
        sample = IP[0:100]
        logger.info(sample)
        for ip in sample:
            remote_host = ip['remote_host']
            self.add(ipinfo,self.IP_INFO,remote_host)
            self.add(abuse,self.ABUSE_IPDB,remote_host)
            self.add(hybrid_analysis,self.HYBRID_ANALYSIS,remote_host)
            self.add(greynoise,'Greynoise',remote_host)
            self.add(ipapi,'IPApi',remote_host)
            self.add(shodan,'Shodan',remote_host)
            self.add(maltiverse,'Maltiverse',remote_host)
            self.add(ipapicom,'IPApiCom',remote_host)
        logger.info(abuse)
        logger.info(hybrid_analysis)
        logger.info(shodan)
        logger.info(ipapi)
        logger.info(ipinfo)
        logger.info(hybrid_analysis)
        logger.info(ipapicom)
        return {
            'ipinfo': ipinfo,
            'shodan': shodan,
            'abuse': abuse,
            'hybrid-analysis': hybrid_analysis,
            'greynoise': greynoise,
            'ipapi': ipapi,
            'ipapicom':ipapicom,
            'maltiverse': maltiverse
        }
        

    def download_IP(self):
        data = sources[self.HONEY_DB].collect()
        process_data = self.process_IP(data['bad-ip'])
        if settings.DEBUG:
            logger.info(data['bad-ip'])
        self.elastic.insert('honeydb-bad-ip',data['bad-ip'])
        self.elastic.insert('ip-info',process_data['ipinfo'])

        self.elastic.insert('abuseipdb',process_data['abuse'])
        self.elastic.insert('shodan',process_data['shodan'])
        self.elastic.insert('hybrid-analysis-host',process_data['hybrid-analysis'])
        self.elastic.insert('greynoise',process_data['greynoise'])
        self.elastic.insert('ipapi',process_data['ipapi'])
        self.elastic.insert('ipapicom',process_data['ipapicom'])
        self.elastic.insert('maltiverse',process_data['maltiverse'])

        

    def download_feed(self):
        self.download_IP()