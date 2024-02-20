import logging
from .feed_downloader import FeedDownloader
from data_collector.apps import sources
from django.conf import settings

logger = logging.getLogger(__name__)


class HybridAnalysisDownloader(FeedDownloader):

    _self = None
    HYBRID_ANALYSIS = 'hybrid-analysis'

    @classmethod
    def init(cls):
        if cls._self is None:
            cls._self = super().__init__(cls)
        return cls._self
    
    def __init__(self) -> None:
        super().__init__()
    

    def download_reports(self):
        data = sources['HybridAnalysis'].collect()
        if settings.DEBUG:
            logger.info(data)
        self.elastic.insert(self.HYBRID_ANALYSIS,data)

        
    def download_feed(self):
        self.download_reports()