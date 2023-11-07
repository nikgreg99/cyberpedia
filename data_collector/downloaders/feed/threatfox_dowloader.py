import logging
from .feed_downloader import FeedDownloader
from data_collector.apps import sources
from django.conf import settings 


logger = logging.getLogger(__name__)

class ThreatFoxDownloader(FeedDownloader):

    _self = None
    THREAT_FOX_MALWARE_LIST = "threatfox-malware-list"

    @classmethod
    def init(cls):
        if cls._self is None:
            cls._self = super().__init__(cls)
        return cls._self
    
    def __init__(self) -> None:
        super().__init__()
    
    def download_feed(self):
        data  = sources["ThreatFox"].collect()
        if settings.DEBUG:
            logger.info(data['ioc'])
            logger.info(data['malware-list'])

        self.elastic.insert('threatfox-ioc',data['ioc'])
       
      
    

