import logging
from .feed_downloader import FeedDownloader
from data_collector.apps import sources

logging = logging.getLogger(__name__)

THREAT_FOX = 'ThreatFox'

class IOCDownloader(FeedDownloader):

    _self = None
    THREAT_FOX = 'ThreatFox'
    THREAT_FOX_MALWARE_LIST = "threat-fox-ioc"


    @classmethod
    def init(cls):
        if cls._self is None:
            cls._self = super().__init__(cls)
        return cls._self

    def __init__(self) -> None:
        super().__init__()
    

    def download_feed(self):
         data_ioc,_= sources[THREAT_FOX].collect()
         self.elastic.insert_data_bulk(self.THREAT_FOX_MALWARE_LIST,data_ioc)
         self.mongo.save_data(self.THREAT_FOX_MALWARE_LIST,data_ioc) 