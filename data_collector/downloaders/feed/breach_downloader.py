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
    
    def download_hashes_by_suffix(self):
        for i in range(int("00000",16),int("FFFFF",16)+ 1):
            prefix = format(i,"05X")


    def download_feed(self):
        data = sources[self.HAVE_I_BEEN_PWNED].collect()
        self.elastic.insert('have-i-been-pwned',data)
        self.mongo.save_data('have-i-been-pwned',data)

