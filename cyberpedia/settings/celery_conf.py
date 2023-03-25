from celery.schedules import crontab

CELERY_BROKER_URL = "redis://localhost:6379"


CELERY_RESULT_BACKEND = "redis://localhost:6379"
CELERY_ACCEPT_CONTENT = ["application/json"]

CELERY_TASK_SERIALIZER = "json"

CELERY_RESULT_SERIALIZER = "json"

CELERY_TIMEZONE = "UTC"
CELERY_TASK_TRACK_STARTED = True

CELERY_IMPORT = ("cyberpedia.tasks",)
CELERY_ALWAYS_EAGER = True

CELERY_BEAT_SCHEDULE = {
   "add-every-day": {
    'task': 'cyberpedia.tasks.update_maldatabase',
    'schedule': crontab(hour=22, minute =  10)
   }
}


