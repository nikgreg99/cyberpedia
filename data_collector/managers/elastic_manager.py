import os
import logging
from .manager import Manager
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

logger = logging.getLogger(__name__)

class ElasticManager(Manager):

    _self = None
    
    def __init__(self) -> None:
            self.elastic = Elasticsearch(os.environ.get('ELASTIC_HOST'),timeout=120)
            self.elastic.info()

    @classmethod
    def init(cls):
        if cls._self is None:
            cls._self = super().__init__(cls)
        return cls._self
        

    def create_index(self,index_name,mappings={}):
        if not self.elastic.indices.exists(index_name):
            self.elastic.indices.create(index=index_name,mappings=mappings)


    def gen_index_data(self,index_name,data):
        for chunck in data:
         yield {
            "_index": index_name,
            "data": chunck
        }

    def insert_data_bulk(self,index_name,data):
     print('ok')
     bulk(self.elastic, self.gen_index_data(index_name,data))
     print("Total number of occurences: ",self.elastic.cat.count(index=index_name,format="json"))


    def create_index(self,name_index):
     if not self.elastic.indices.exists(index=name_index):
            self.elastic.indices.create(index=name_index)

    def delete_index(self,name_index):
        if not self.elastic.indices.exists(index=name_index):
            self.elastic.indices.delete(index=name_index)


    def create_data_indexes(self,indexes):
        for index in indexes:
            self.create_index(index)
       