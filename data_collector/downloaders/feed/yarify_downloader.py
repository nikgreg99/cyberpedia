import logging
from .feed_downloader import FeedDownloader
from data_collector.apps import sources

logger = logging.getLogger(__name__)


class YarifyDownloader(FeedDownloader):

    _self = None
    YARIFY = "Yarify"


    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def init(cls):
        if cls._self is None:
            cls._self = super().__init__(cls)
        return cls._self
    
    def download_feed(self):
        data = sources[self.YARIFY].collect()
        self.elastic.insert_data_bulk(self.YARIFY.lower(),data)
        self.mongo.save_data(self.YARIFY.lower(),data)

