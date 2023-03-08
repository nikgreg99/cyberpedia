import dataclasses
import typing

@dataclasses.dataclass
class _Secret:
    env_var_key : str
    required:  bool

@dataclasses.dataclass
class CollectorConfig:
    name: str
    secrets: typing.Dict[str, _Secret]