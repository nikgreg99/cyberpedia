import os
import logging
from .manager import Manager
from pymongo import MongoClient


logger = logging.getLogger(__name__)

class MongoManager(Manager):

    _self = None

    @classmethod
    def init(cls):
        if cls._self is None:
            cls._self = super().__init__(cls)
        return cls._self

    def __init__(self) -> None:
        self.mongo = MongoClient(os.environ.get('MONGO_URL'))
        self.mongo_db = self.mongo[os.environ.get('MONGO_NAME')]


    def get_db(self):
        return self.mongo_db

    def create_collections(self,collection_names:list):
        for collection_name in collection_names:
           collection = self.mongo_db[collection_name]


    def save_data(self,collection_name,data):
        print(data)
        collection = self.mongo_db[collection_name]
        doc = collection.insert_many(data)


    def save_data_one(self,collection_name,data):
        collection = self.mongo_db[collection_name]
        doc = collection.insert_one(data)

    
    
    
    

     
