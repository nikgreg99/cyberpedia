import logging
from .feed_downloader import FeedDownloader
from data_collector.apps import sources


logger = logging.getLogger(__name__)


class BreachDownloader(FeedDownloader):

    _self = None
    HAVE_I_BEEN_PWNED = "HaveIBeenPwned"

    @classmethod
    def init(cls):
        if cls._self is None:
            cls._self = super().__init__(cls)
        return cls._self


    def download_feed(self):
        data = sources[self.HAVE_I_BEEN_PWNED].collect()
        self.elastic.insert_data_bulk('have-i-been-pwned',data)
        self.mongo.save_data('have-i-been-pwned',data)

