import dataclasses
import typing
from .models import APIConfig,Feed
from django.conf import settings

@dataclasses.dataclass
class _Param:
    name : str
    type: str
    description: str

@dataclasses.dataclass
class _Secret:
    env_var_key : str
    required:  bool


@dataclasses.dataclass
class CollectorConfig:

    name: str
    secrets: typing.Dict[str, _Secret]
    parameters: typing.Dict[str, _Param]

    def __init__(self,name) -> None:
        self.name = name


    def read_secrets(self ) -> dict:
        secrets = {}
        feed = Feed.objects.get(name = self.name)
        configs = APIConfig.objects.filter(collector__pk=feed.pk)
        for config in configs:
            secrets[config.name] = config.value
        return secrets

    def read_paramters(self):
        pass






   
   