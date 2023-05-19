import logging
from .downloader import DataDownloader
from data_collector.sources.apps import sources

logger = logging.getLogger(__name__)


class YaraDownloader(DataDownloader):

    _self = None
    YARIFY = "Yarify"


    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def init(cls):
        if cls._self is None:
            cls._self = super().__init__(cls)
        return cls._self
    
    def download_data(self):
        data = sources["Yarify"].collect()
        self.elastic.insert_data_bulk("yarify",data)
        self.mongo.save_data("yarify",data)

