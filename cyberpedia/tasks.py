import logging
from data_collector.download.download_ip import IPDownloader
from data_collector.sources.apps import sources
from data_collector.managers.mongo_manager import MongoManager
from data_collector.managers.elastic_manager import ElasticManager
from cyberpedia.celery import app

logger = logging.getLogger(__name__)
mongo = MongoManager()
elastic = ElasticManager()

MALDATABASE= 'Maldatabase'

@app.task()
def updateMalpediaFeed():
    data = sources["Maldatabase"].collect()
    print(data)
    elastic.insert_data_bulk("maldatabase",data)
    mongo.save_data("maldatabase",data)
    


    
   


   



    
    



