import logging
from data_collector.download.download_ip import IPDownloader
from data_collector.download.download_yara import YaraDownloader
from data_collector.download.download_ioc import IOCDownloader
from data_collector.download.download_malware import MalwareDownloader
from data_collector.download.download_breaches import BreachDownloader
from cyberpedia.celery import app

logger = logging.getLogger()

def updateIP():
    ip_downloader = IPDownloader
    ip_downloader.download_data()



def updateYara():
    yara = YaraDownloader()
    yara.download_data()


def updateIOC():
   ioc = IOCDownloader()
   ioc.download_data()



def updateMalware():
    malware = MalwareDownloader()
    malware.download_data()
    
@app.task()
def update_breaches():
    breach = BreachDownloader()
    breach.download_data()
    
    
   


   



    
    



