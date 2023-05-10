import logging
from .data_download import DataDownloader
from data_collector.sources.apps import sources
from data_collector.managers.elastic_manager import ElasticManager
from data_collector.managers.mongo_manager import MongoManager

logger = logging.getName(__name__)


HONEY_DB = 'Honey_DB'
SHODAN = 'Shodan'
IP_INFO = 'IPinfo'
ABUSE_IPDB = 'AbuseIPDB'

class IPDownloader(DataDownloader):

    _self = None

    @classmethod
    def init(cls):
        if cls._self is None:
            cls._self = super().__init__(cls)
        return cls._self
    
    def process_IP(self,list_IP):
        shodan = []
        ip_info = []
        abuse_ipdb = []
        for ip in list_IP:
            remote_host = ip['remote_host']
            ip_info.append(sources[IP_INFO].collect_targert(remote_host))
            shodan.append(sources[SHODAN].collect_target(remote_host))
            abuse_ipdb.append(sources[ABUSE_IPDB].collect_target(remote_host))


    def download_IP(self):
        bad_id, twitter_feed = sources[HONEY_DB].collect()
        self.process_IP(bad_id)
        self.process_IP(twitter_feed)
        

    def download_data(self):
        self.download_IP()