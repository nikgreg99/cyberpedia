import logging
from data_collector.downloaders.feed.breach_downloader import BreachDownloader
from data_collector.downloaders.feed.valhalla_downloader import ValhallaDownloader
from data_collector.downloaders.feed.yarify_downloader import YarifyDownloader
from data_collector.downloaders.feed.ioc_downloader import IOCDownloader
from data_collector.downloaders.feed.payload_downloader import PayloadDownloader
from data_collector.downloaders.feed.ip_downloader import IPDownloader
from data_collector.downloaders.feed.url_downloader import URLDownloader
from cyberpedia.celery import shared_task

logger = logging.getLogger(__name__)

@shared_task()
def update_breaches():
    breach_downloader = BreachDownloader()
    breach_downloader.download_feed()
    logger.info("Breaches updated succesfully")


@shared_task()
def update_valhalla():
    valhalla = ValhallaDownloader()
    valhalla.download_feed()
    logger.info("Valhalla updated succesfully")

@shared_task()
def update_yarify():
    yarify = YarifyDownloader()
    yarify.download_feed()
    logger.info("Yarify rules updated succesfully")

@shared_task()
def update_IOC():
    ioc_downloader = IOCDownloader()
    ioc_downloader.download_feed()
    logger.info("IOC updated succesfully")

@shared_task()
def update_payload():
    payload_downloader = PayloadDownloader()
    payload_downloader.download_feed()
    logger.info('Payloads updated succesfully')


@shared_task()
def update_IP():
    ip_downloader = IPDownloader()
    ip_downloader.download_feed()
    logger.info('IP data updated succesfully')


@shared_task()
def update_URL():
    url_downloader = URLDownloader()
    url_downloader.download_feed()
    logger.info('URL data updated succesfully')



    


    
   


   



    
    



