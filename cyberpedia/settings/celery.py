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
        'schedule': crontab(hour="0",minute="0")
    },
    'update-malware': {
        'task': 'cyberpedia.tasks.update_malware',
        'schedule': crontab(hour='0', minute='15')
    },
    'update-breaches': {
        'task': 'cyberpedia.tasks.update_breaches',
        'schedule': crontab(hour='0', minute='30')
    },
    'update-IOC': {
        'task': 'cyberperdia.tasks.update_IOC',
        'schedule': crontab(minute="*/30")
    },
    'update-yara': {
        'task': 'cyberpedia.tasks.update_yara',
        'schedule': crontab(minute="*/15")
    },
    'update-valhalla': {
        'task': 'cyberpedia.tasks.update_valhalla',
        'schedule': crontab(hour="1",minute="30")
    },
    "update-URL": {
        'task': 'cyberpedia.tasks.update_URLHaus',
        'schedule': crontab(hour='*/1')
    },
    'update-payload': {
        'task': 'cyberpedia-tasks,update_payload',
        'schedule': crontab(hour='0',minute='45')
    }
}


