import logging
from data_collector.downloaders.yara_downloader import YaraDownloader
from data_collector.downloaders.ip_downloader import IPDownloader
from data_collector.downloaders.url_downloader import URLDownloader
from cyberpedia.celery import app

logger = logging.getLogger(__name__)


@app.task()
def update_yara():
    yara = YaraDownloader()
    yara.download_data()

@app.task()
def update_IP():
    ip = IPDownloader()
    ip.download_data()

@app.task()
def update_URL():
    url_downloader = URLDownloader()
    url_downloader.download_data()







    


    
   


   



    
    



