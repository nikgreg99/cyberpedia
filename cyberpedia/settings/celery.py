import os
from dotenv import load_dotenv
from .common import CONFIG_DIR
from celery.schedules import crontab

dotenv_path = os.path.join(CONFIG_DIR,"celery.env")
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
    'update-yarify': {
        'task': 'cyberpedia.tasks.update_yarify',
        'schedule': crontab(minute = '*/2')
   },
   'update-IOC': {
       'task': 'cyberpedia.tasks.update_IOC',
       'schedule': crontab(minute="*/2")
   },
   'update-payload': {
       'task': 'cyberpedia.tasks.update_payload',
       'schedule': crontab(minute='*/2')
   },
   'update-IP': {
       'task': 'cyberpedia.tasks.update_IP',
       'schedule': crontab(minute="*/2")
   },
   'upload-valhalla':{
       'task': 'cyberpedia.tasks.update_valhalla',
       'schedule': crontab(minute = '*/3')
   }
}



