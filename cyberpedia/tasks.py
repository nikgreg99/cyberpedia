import logging
from data_collector.download.download_ip import IPDownloader
from data_collector.download.download_yara import YaraDownloader
from data_collector.download.download_ioc import IOCDownloader
from data_collector.download.download_malware import MalwareDownloader

logger = logging.getLogger(__name__)


#Feed downloads

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
    
    
    
   


   



    
    



