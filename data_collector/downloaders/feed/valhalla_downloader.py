import logging
from .feed_downloader import FeedDownloader
from data_collector.apps import sources

class ValhallaDownloader(FeedDownloader):
    _self = None
    VALHALLA = "Valhalla"
    VALHALLA_YARA = "Valhalla-Yara"
    VALHALLA_SIGMA = "Valhalla-Sigma"


    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def init(cls):
        if cls._self is None:
            cls._self = super().__init__(cls)
        return cls._self
    
    def download_feed(self):
        yara_json, sigma_json = sources[self.VALHALLA].collect()
        self.elastic.insert_data_bulk(self.VALHALLA_YARA.lower(),yara_json)
        self.elastic.insert_data_bulk(self.VALHALLA_SIGMA.lower(),sigma_json)
        self.mongo.save_data(self.VALHALLA_YARA.lower(),yara_json)
        self.mongo.save_data(self.VALHALLA_SIGMA.lower(),sigma_json)
        