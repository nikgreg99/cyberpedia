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
CELERY_RESULT_SERIALIZER = os.environ.get('CELERY__RESULT_SERIALIZER')
CELERY_TIMEZONE = os.environ.get('CELERY_TIMEZONE')


CELERY_BEAT_SCHEDULE = {
   'updateIP': {
    'task': 'cyberpedia.tasks.updateIP',
    'schedule': crontab(hour=0, minute =  0)
   },
   'updateYara': {
      'task': 'cyberpedia.tasks.updateYara', 
      'schedule': crontab(minute='*/30')
   },
   'updateIOC': {
       'task': 'cyberpedia.tasks.updateIOC',
       'schedule': crontab(hour = 0, minute = 0)
   },
   'updateMalware': {
       'task': 'cyperbedia.tasks.updateMalware',
       'schedule': crontab(hour = 1, minute = 0)
   }
   
}



