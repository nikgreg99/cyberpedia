import logging
from data_collector.managers.manager import Manager
from data_collector.managers.mongo_manager import MongoManager
from data_collector.managers.elastic_manager import ElasticManager


logger = logging.getLogger(__name__)

class SynchManager(Manager):

    _self = None
    
    def __init__(self) -> None:
        self.mongo = MongoManager()
        self.elastic = ElasticManager()

    @classmethod
    def init(cls):
        if cls._self is None:
            cls._self = super().__init__(cls)
        return cls._self
    
    def sync_index(self,collection_name):
        collection = self.mongo.get_db[collection_name]
        cursor = collection.find()
        self.elastic.insert(collection_name,cursor)

    def sync(self,indexes):
        for index in indexes:
            self.sync_index(index)