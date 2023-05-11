import logging

logger = logging.getLogger(__name__)
from data_collector.managers.elastic_manager import ElasticManager
from data_collector.managers.mongo_manager import MongoManager

class DataDownloader(object):

    def __init__(self) -> None:
        pass

    def download_data(self):
        pass