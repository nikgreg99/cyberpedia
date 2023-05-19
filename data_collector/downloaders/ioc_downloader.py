import logging
from .downloader import DataDownloader
from data_collector.sources.apps import sources

logging = logging.getLogger(__name__)

THREAT_FOX = 'ThreatFox'

class IOCDownloader(DataDownloader):

    _self = None
    THREAT_FOX = 'ThreatFox'


    @classmethod
    def init(cls):
        if cls._self is None:
            cls._self = super().__init__(cls)
        return cls._self

    def __init__(self) -> None:
        super().__init__()
    
    def download_data_ioc():
        data_ioc = sources[THREAT_FOX].collect()



    def download(self):
        self.download_data_ioc()