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

CELERY_BEAT_SCHEDULE = {
    'update-IP': {
        'task': 'cyberpedia.tasks.update_IP',
        'schedule': crontab(minute=0,hour='*/12')
    },
    'update-CVE': {
        'task': 'cyberpedia.tasks.update_CVE',
        'schedule': crontab(hour=0,minute=30)
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
        'schedule': crontab(minute=0,hour='*/1')
    },
    'process_IPInfo': {
        'task' :'cyberpedia.tasks.process_IPInfo',
        'schedule': crontab(minute=20,hour=0)
    },
    'process_IPApi': {
        'task': 'cyberpedia.tasks.process_IPApi',
        'schedule': crontab(minute=0,hour='*/6')
    },
    'process_IPApiCom': {
        'task': 'cyberpedia.tasks.process_IPApiCom',
        'schedule': crontab(hour=18,minute=25)
    },
    'process_AbuseIPDB': {
        'task': 'cyberpedia.tasks.process_AbuseIPDB',
        'schedule': crontab(hour=0,minute=40)
    },
    'process_HybridAnalysis': {
        'task': 'cyberpedia.tasks.process_HybridAnalysis',
        'schedule': crontab(minute=0,hour='*/4')
    }
}


