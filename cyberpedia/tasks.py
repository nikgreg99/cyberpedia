import zipfile
import logging
from celery import app
from data_collector.sources.apps import sources
from data_collector.models import DataFeed

logger = logging.getLogger(__name__)

#Feed downloads

@app.task
def honeydb_twitter_feed():
   raw_data = sources["HoneyDB"].collect_twitter_feed()

@app.task
def honeydb_bad_ip():
   raw_data = sources["HoneyDB"].collect_bad_ip()

@app.task
def haveibeen_pwned():
   raw_data = sources["HaveIBeenPwened"].collect() 

@app.task 
def threat_fox_ioc():
    raw_data = sources["ThreatFox"].query_recent_IOC()

@app.task
def yarify():
    raw_data = sources["Yarify"].list_recent_deployed_rules()


@app.task
def valhalla_yara():
   response = sources["Valhalla"].download_public_yara_rules()
   with zipfile.ZipFile("", 'r') as zip_ref:
         zip_ref.extractall("")
   

@app.task
def valhalla_sigma():
   response = sources["Valhalla"].download_public_sigma_rules()
   with zipfile.ZipFile("", 'r') as zip_ref:
         zip_ref.extractall("")
      
def urlhaus_urls():
    raw_data = sources["UrlHaus"].query_recent_urls()

def urlhaus_payloads():
    raw_data = sources["UrlHaus"].query_recent_payloads()
    
   
   



    
    



