import logging
from data_collector.downloaders.feed.breach_downloader import BreachDownloader
from data_collector.downloaders.feed.valhalla_downloader import ValhallaDownloader
from data_collector.downloaders.feed.yara_downloader import YaraDownloader
from data_collector.downloaders.feed.ioc_downloader import IOCDownloader
from data_collector.downloaders.feed.payload_downloader import PayloadDownloader
from data_collector.downloaders.feed.ip_downloader import IPDownloader
from data_collector.downloaders.feed.urlhaus_downloader import URLHausDownloader
from data_collector.downloaders.feed.threatfox_dowloader import ThreatFoxDownloader
from data_collector.downloaders.feed.opencve_downloader import OpenCVEDownloader
from django.conf import settings
from cyberpedia.celery import shared_task

logger = logging.getLogger(__name__)

@shared_task()
def update_URLHaus():
    urlhaus = URLHausDownloader()
    urlhaus.download_feed()
    if settings.DEBUG:
        logger.info("UrlHaus feeds updated succesfully")

@shared_task()
def update_breaches():
    breach_downloader = BreachDownloader()
    breach_downloader.download_feed()
    if settings.DEBUG:
        logger.info("Breaches updated succesfully")


@shared_task()
def update_valhalla():
    valhalla = ValhallaDownloader()
    valhalla.download_feed()
    if settings.DEBUG:
        logger.info("Valhalla updated succesfully")

@shared_task()
def update_yara():
    yarify = YaraDownloader()
    yarify.download_feed()
    if settings.DEBUG:
        logger.info("Yarify rules updated succesfully")

@shared_task()
def update_IOC():
    ioc_downloader = IOCDownloader()
    ioc_downloader.download_feed()
    if settings.DEBUG:
        logger.info("IOC updated succesfully")

@shared_task()
def update_payload():
    payload_downloader = PayloadDownloader()
    payload_downloader.download_feed()
    if settings.DEBUG:
        logger.info('Payloads updated succesfully')


@shared_task()
def update_IP():
    ip_downloader = IPDownloader()
    ip_downloader.download_feed()
    if settings.DEBUG:
        logger.info('IP data updated succesfully')


@shared_task()
def update_threatfox():
    threatfox = ThreatFoxDownloader()
    threatfox.download_feed()
    if settings.DEBUG:
        logger.info('ThreatFox feeds update succesfully')

@shared_task()
def update_URL():
    url_downloader = URLHausDownloader()
    url_downloader.download_feed()
    if settings.DEBUG:
        logger.info('URL data updated succesfully')

@shared_task()
def update_vulns():
    opencve = OpenCVEDownloader()
    opencve.download_feed()
    if settings.DEBUG:
        logger.info('Vulnerability records updated successfully')





    


    
   


   



    
    



