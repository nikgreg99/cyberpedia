import os
from dotenv import load_dotenv
from .common import CONFIG_DIR

dotenv_path = os.path.join(CONFIG_DIR,"celery.env")
load_dotenv(dotenv_path)
from celery.schedules import crontab


CELERY_BROKER_URL = os.environ.get('CELERY_BROKEN_URL') 
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND') 
CELERY_ACCEPT_CONTENT = [os.environ.get('CELERY_ACCEPT_CONTENT')]

CELERY_TASK_SERIALIZER = os.environ.get('CELERY_TASK_SERIALIZER')

CELERY_RESULT_SERIALIZER = os.environ.get('CELERY_TASK_RESULT_SERIALIZER')

CELERY_TIMEZONE = os.environ.get('CELERY_TIMEZONE')
CELERY_TASK_TRACK_STARTED = os.environ.get('CELERY_TASK_TRACK_STARTED')

CELERY_IMPORT = (os.environ.get('CELERY_IMPORT'),)
CELERY_ALWAYS_EAGER = os.environ.get('CELERY_ALWAYS_EAGER')

CELERY_BEAT_SCHEDULE = {
   "add-every-day": {
    'task': 'cyberpedia.tasks.update_maldatabase',
    'schedule': crontab(hour=22, minute =  10)
   }
}


