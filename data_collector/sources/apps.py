from django.apps import AppConfig
import importlib


sources = {}

def start_up():
    global sources
    from data_collector.models import Feed
    api_module = importlib.import_module('data_collector.sources.api')
    collector_names = Feed.collector_names()
    for collector_name in collector_names:
        name = collector_name["name"]
        api_module = importlib.import_module('data_collector.sources.api.{}'.format(name.lower()))
        klass = getattr(api_module,name)
        api_instance = klass()
        sources[name] = api_instance
        api_instance.init_collector()


class SourcesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'data_collector.sources'

    def ready(self) -> None:
        start_up()

