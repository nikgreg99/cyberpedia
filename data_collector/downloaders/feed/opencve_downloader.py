import logging
from .feed_downloader import FeedDownloader
from data_collector.apps import sources
from django.conf import settings


logging = logging.getLogger(__name__)

class OpenCVEDownloader(FeedDownloader):

    self = None

    @classmethod
    def init(cls):
        if cls._self is None:
            cls._self = super().__init__(cls)
        return cls._self
    
    def __init__(self) -> None:
        super().__init__()
    
    def download_feed(self):
        data = sources['OpenCVE'].collect()
        self.elastic.insert('opencve-cve',data['cve'])
    