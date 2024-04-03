import os
from dotenv import load_dotenv
from .common import CONFIG_DIR
from celery.schedules import crontab

dotenv_path = os.path.join(CONFIG_DIR, "celery.env")
load_dotenv(dotenv_path)


CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND')
CELERY_ACCEPT_CONTENT = [os.environ.get('CELERY_ACCEPT_CONTENT')]
CELERY_TASK_SERIALIZER = os.environ.get('CELERY_TASK_SERIALIZER')
CELERY_RESULT_SERIALIZER = os.environ.get('CELERY_RESULT_SERIALIZER')
CELERY_ALWAYS_EAGER = os.environ.get('CELERY_ALWAYS_EAGER')
CELERY_TIMEZONE = os.environ.get('CELERY_TIMEZONE')
CELERY_TASK_TRACK_STARTED = os.environ.get('CELERY_TASK_TRACK_STARTED')
CELERY_IGNORE_RESULT = os.environ.get('CELERY_IGNORE_RESULT')
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = os.environ.get('CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP')

CELERY_BEAT_SCHEDULE = {
    'update-IP': {
        'task': 'cyberpedia.tasks.update_IP',
        'schedule': crontab(minute=0,hour='*/12')
    },
    'update-CVE': {
        'task': 'cyberpedia.tasks.update_CVE',
        'schedule': crontab(minute="*/15")
    },
    'update-breaches': {
        'task': 'cyberpedia.tasks.update_breaches',
        'schedule': crontab(hour=0, minute=20)
    },
    'update-IOC': {
        'task': 'cyberpedia.tasks.update_IOC',
        'schedule': crontab(minute=0,hour='*/1')
    },
     "update-URL": {
        'task': 'cyberpedia.tasks.update_URLHaus',
        'schedule': crontab(minute=0,hour='*/2')
    },
    'update-yara': {
        'task': 'cyberpedia.tasks.update_yara',
        'schedule': crontab(minute='*/15')
    },
    'update-valhalla': {
        'task': 'cyberpedia.tasks.update_valhalla',
        'schedule': crontab(hour=0,minute=40)
    },
    'update_HybridAnalysis': {
        'task': 'cyberpedia.tasks.update_HybridAnalysis',
        'schedule': crontab(minute='0',hour=1)
    },
    'update_MalwareBaazar': {
        'task': 'cyberpedia.tasks.update_MalwareBaazar',
        'schedule': crontab(minute=0,hour='*/1')
    },
    'update_FeodoTracker':  {
        'task': 'cyberpedia.tasks.update_FeodoTracker',
        'schedule': crontab(minute='*/15')
    },
    'process_IPInfo': {
        'task' :'cyberpedia.tasks.process_IPInfo',
        'schedule': crontab(minute=0,hour=1)
    },
    'process_IPApi': {
        'task': 'cyberpedia.tasks.process_IPApi',
        'schedule': crontab(minute=0,hour=2)
    },
    'process_IPApiCom': {
        'task': 'cyberpedia.tasks.process_IPApiCom',
        'schedule': crontab(hour=18,minute=25)
    },
    'process_AbuseIPDB': {
        'task': 'cyberpedia.tasks.process_AbuseIPDB',
        'schedule': crontab(hour=0,minute=40)
    },
    'process_Shodan': {
        'task': 'cyberpedia.tasks.process_Shodan',
        'schedule': crontab(minute=0,hour='*/1')
    },
    'process_HybridAnalysis': {
        'task': 'cyberpedia.tasks.process_HybridAnalysis',
        'schedule': crontab(minute=0,hour='*/3')
    },
    'process_Greynoise': {
        'task': 'cyberpedia.tasks.process_GreyNoise',
        'schedule': crontab(minute=30,hour=11)
    },
    'process_Maltiverse_IP': {
        'task': 'cyberpedia.tasks.process_Maltiverse_IP',
        'schedule': crontab(hour=1,minute=40)
    },
    'process_Virus_Total_IP': {
        'task': 'cyberpedia.tasks.process_VirusTotal_IP',
        'schedule': crontab(minute=0,hour='*/1')
    },
    'process_HybridAnalysis_URL' : {
        'task': 'cyberpedia.tasks.process_HybridAnalysis_URL',
        'schedule': crontab(minute=0,hour= '*/5')
    },
    'process_UrlScan':{
        'task': 'cyberpedia.tasks.process_UrlScan',
        'schedule': crontab(hour=5,minute=0)
    },
    'process_Censys': {
        'task': 'cyberpedia.tasks.process_Censys',
        'schedule': crontab(minute=0,hour='*/3')
    }
}


