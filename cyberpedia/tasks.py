import logging
from data_collector.downloaders.feed.breach_downloader import BreachDownloader
from data_collector.downloaders.feed.valhalla_downloader import ValhallaDownloader
from data_collector.downloaders.feed.yarify_downloader import YarifyDownloader
from cyberpedia.celery import app

logger = logging.getLogger(__name__)

@app.task
def update_breaches():
    breach_downloader = BreachDownloader()
    breach_downloader.download_feed()
    logger.info("Breaches update succesfully")


@app.task
def update_valhalla():
    valhalla = ValhallaDownloader()
    valhalla.download_feed()
    logger.info("Valhalla updates succesfully")
    
@app.task
def update_yarify():
    yarify = YarifyDownloader()
    yarify.download_feed()
    logger.info("Yarify updates succesfully")







    


    
   


   



    
    



