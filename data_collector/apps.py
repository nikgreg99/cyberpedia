import logging
import importlib
from django.apps import AppConfig

logger = logging.getLogger(__name__)

sources = {}

class DataCollectorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'data_collector'
    verbose_name = "DataCollector"

    def ready(self):
        global sources
        from data_collector.models import Feed
        api_module = importlib.import_module('data_collector.sources.api')
        collector_names = Feed.collector_names()
        
        for collector_name in collector_names:
            name = collector_name["name"]
            try:
                api_module = importlib.import_module('data_collector.sources.api.{}'.format(name.lower()))
                if api_module is not None:
                    klass = getattr(api_module,name)
                    api_instance = klass()
                    sources[name] = api_instance
            except ModuleNotFoundError as ex:
                    logger.exception(f"{collector_name} cannot be found or doesn't exists")




  




