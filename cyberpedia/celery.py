from __future__ import absolute_import, unicode_literals
import os 
from celery import Celery,shared_task
from django.apps import apps


os.environ.setdefault("DJANGO_SETTINGS_MODULE","cyberpedia.settings")
app = Celery("cyberpedia")
app.config_from_object('django.conf:settings',namespace='CELERY')

app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])


#Debug task: Just for making sure Celery is up and running!
@shared_task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


