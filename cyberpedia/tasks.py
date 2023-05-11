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
YARIFY = 'Yarify'
VALHALLA = 'Valhalla'

@app.task()
def updateMalpediaFeed():
    data = sources["Maldatabase"].collect()
    print(data)
    elastic.insert_data_bulk("maldatabase",data)
    mongo.save_data("maldatabase",data)


@app.task()
def updateIPFeed():
    ip_feed = IPDownloader()
    ip_feed.download_data()

@app.task()
def updateYara():
    data = sources['Yarify'].collect()
    elastic.insert_data_bulk("yarify",data)
    mongo.save_data("yarify",data)

@app.task
def updateValhalla():
    yara,sigma = sources[VALHALLA].collect()
    mongo.save_data('valhalla-yara',yara)
    mongo.save_data("valhalla-sigma",sigma)



    


    
   


   



    
    



