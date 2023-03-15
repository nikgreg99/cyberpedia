import dataclasses
import typing
from .models import Config



@dataclasses.dataclass
class _Secret:
    env_var_key : str
    required:  bool


@dataclasses.dataclass
class CollectorConfig:

    name: str
    description: str
    secrets: typing.Dict[str, _Secret]


    def read_secrets(self,secret_filter=None) -> dict: 
        if secret_filter is None:
            pass
        secrets = {}
        configs = Config.objects.filter(collector_name = self.name)
        for config in configs.values:
            secrets[config.type] = config.value
        return secrets







   
   