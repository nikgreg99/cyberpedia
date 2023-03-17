import logging
from celery import signals
from celery import shared_task
logger = logging.getLogger(__name__)


@shared_task
def build_collector_cache(*args,**kwargs):
    logger.info("Worker correctly")
    collectors = []
    from data_collector.models import APIConfig
    collector_names = APIConfig.collector_names()
    for collector_name in collector_names:
        collector = __import__("datacollector.sources.api.{}".format(collector_name))
        collector.init_collector()
        collectors.append(collector)
    return collectors

#startapp
@signals.worker_ready.connect
def init_collector(self):
    build_collector_cache()


