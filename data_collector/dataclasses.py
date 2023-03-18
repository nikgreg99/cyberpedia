import dataclasses
import typing
from .models import APIConfig



@dataclasses.dataclass
class _Secret:
    env_var_key : str
    required:  bool


@dataclasses.dataclass
class CollectorConfig:

    name: str
    secrets: typing.Dict[str, _Secret]

    def __init__(self,name) -> None:
        self.name = name

    def read_secrets(self ) -> dict:
        secrets = {}
        configs = APIConfig.objects.filter(name = self.name)
        for config in configs.values():
            secrets[config.type] = config.value
        return secrets







   
   