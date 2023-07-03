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


CELERY_BEAT_SCHEDULE = {
   'update_breaches': {
    'task': 'cyberpedia.tasks.update_breaches',
    'schedule': crontab(minute=0, hour=0),
   },
   'update-valhalla': {
       'task': 'cyberpedia.tasks.update_valhalla',
       'schedule': crontab(minute=0, hour=0),
   },
   'update-yarify': {
        'task': 'cyberpedia.tasks.update_yarify',
        'schedule': crontab(minute=0, hour=1)
   }
}



