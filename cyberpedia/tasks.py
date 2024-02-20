import logging
from data_collector.downloaders.feed.breach_downloader import BreachDownloader
from data_collector.downloaders.feed.valhalla_downloader import ValhallaDownloader
from data_collector.downloaders.feed.yara_downloader import YaraDownloader
from data_collector.downloaders.feed.ioc_downloader import IOCDownloader
from data_collector.downloaders.feed.ip_downloader import IPDownloader
from data_collector.downloaders.feed.urlhaus_downloader import URLHausDownloader
from data_collector.downloaders.feed.threatfox_dowloader import ThreatFoxDownloader
from data_collector.downloaders.feed.nve import NVECollector
from data_collector.downloaders.feed.malware_downloader import MalwareDownloader
from data_collector.downloaders.feed.hybrid_analysis_downloader import HybridAnalysisDownloader

from data_collector.processors.ip_processor import IPProcessor

from data_collector.benchmarkers.index_benchmark import IndexStorageGrowthBenchmark


from django.conf import settings
from cyberpedia.celery import shared_task

logger = logging.getLogger(__name__)


@shared_task()
def monitor_indexes():
    monitor = IndexStorageGrowthBenchmark()
    monitor.monitor_benchmark()

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
    yaraify = YaraDownloader()
    yaraify.download_feed()
    if settings.DEBUG:
        logger.info("Yarify rules updated succesfully")

@shared_task()
def update_MalwareBaazar():
    malware_baazar = MalwareDownloader()
    malware_baazar.download_feed()
    if settings.DEBUG:
        logger.info("Malware Feed downloaded")

@shared_task()
def update_IOC():
    ioc_downloader = IOCDownloader()
    ioc_downloader.download_feed()
    if settings.DEBUG:
        logger.info("IOC updated succesfully")


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
def update_HybridAnalysis():
    hybrid_analysis = HybridAnalysisDownloader()
    hybrid_analysis.download_feed()

@shared_task()
def update_URL():
    url_downloader = URLHausDownloader()
    url_downloader.download_feed()
    if settings.DEBUG:
        logger.info('URL data updated succesfully')

@shared_task()
def update_CVE():
    nve = NVECollector()
    nve.download_feed()
    if settings.DEBUG:
        logger.info('CVE records updated successfully')

@shared_task()
def update_malware():
    malware = MalwareDownloader()
    malware.download_feed()
    if settings.DEBUG:
        logger.info("Malware data updatetd succesfully")


@shared_task()
def process_IPInfo():
    processor = IPProcessor("IPInfo",1500)
    processor.process_data()
    if settings.DEBUG:
        logger.info('IPInfo data processed')

@shared_task()
def process_IPApi():
    processor = IPProcessor("IPApi",100)
    processor.process_data()

@shared_task()
def process_IPApiCom():
    processor = IPProcessor("IPApiCom",50)
    processor.process_data()

@shared_task()
def process_AbuseIPDB():
    processor = IPProcessor('AbuseIPDB',950)
    processor.process_data()

@shared_task()
def process_HybridAnalysis():
    processor=  IPProcessor('HybridAnalysis',2000)
    processor.process_data()

@shared_task()
def process_Shodan():
    processor = IPProcessor('Shodan',100)
    processor.process_data()

@shared_task()
def process_GreyNoise():
    processor = IPProcessor('Greynoise',16)
    processor.process_data()

@shared_task()
def process_Maltiverse_IP():
    processor = IPProcessor('Maltiverse',100)
    processor.process_data()




    


    
   


   



    
    



