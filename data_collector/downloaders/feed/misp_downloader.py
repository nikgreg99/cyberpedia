import logging
from .feed_downloader import FeedDownloader
from data_collector.sources.connectors.misp  import MISPConnector
from data_collector.sources.apps import sources

logger = logging.getLevelName(__name__)

class MISPDownloader(FeedDownloader):

    _self = None

    @classmethod
    def init(cls):
        if cls._self is None:
            cls._self = super().__init__(cls)
        return cls._self
    
    def __init__(self) -> None:
        self.misp = MISPConnector()
        super().__init__()
    
    def download_feed(self):
        pass