import logging
from .feed_downloader import FeedDownloader

logger = logging.getLogger(__name__)

class ThreatJammerDownloader(FeedDownloader):
    
    def __init__(self) -> None:
        super().__init__()

    def download_feed(self):
        return super().download_feed()