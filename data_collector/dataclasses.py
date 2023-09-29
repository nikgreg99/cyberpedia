import dataclasses
import typing
from .models import APIConfig

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
        configs = APIConfig.objects.filter(name = self.name)
        for config in configs:
            secrets[config.type] = config.value
        return secrets

    def read_paramters(self):
        pass






   
   