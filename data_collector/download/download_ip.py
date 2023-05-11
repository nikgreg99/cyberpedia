import logging
from .data_download import DataDownloader
from data_collector.sources.apps import sources
from data_collector.managers.elastic_manager import ElasticManager
from data_collector.managers.mongo_manager import MongoManager


HONEY_DB = 'HoneyDB'
SHODAN = 'Shodan'
IP_INFO = 'IPInfo'
ABUSE_IPDB = 'AbuseIPDB'
HYBRID_ANALYSIS = 'HybridAnalysis'
MALTIVERSE = 'Maltiverse'

mongo = MongoManager()
elastic = ElasticManager()
class IPDownloader(DataDownloader):

    _self = None

    @classmethod
    def init(cls):
        if cls._self is None:
            cls._self = super().__init__(cls)
        return cls._self
    
    def append_list(self,list,key,ip):
        result = sources[key].collect_target(ip)
        print(result)
        list.append(result)
    
    def process_IP(self,list_IP):
        shodan =  []
        ip_info = []
        abuse_ipdb = []
        hb_ip = []
        maltiverse = []
        for ip in list_IP:
            remote_host = ip['remote_host']
            self.append_list(shodan,SHODAN,remote_host)
            self.append_list(ip_info,IP_INFO,remote_host)
            self.append_list(abuse_ipdb,ABUSE_IPDB,remote_host)
            self.append_list(hb_ip,HYBRID_ANALYSIS,remote_host)
            self.append_list(maltiverse,MALTIVERSE,remote_host)

        


    def download_IP(self):
        bad_id, twitter_feed = sources[HONEY_DB].collect()
        self.process_IP(bad_id)
        self.process_IP(twitter_feed)
        

    def download_data(self):
        self.download_IP()