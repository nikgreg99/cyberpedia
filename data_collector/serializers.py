import os
import json


from rest_framework import serializers as rfs
from django.conf import settings


class _SecretSerializer(rfs.Serializer):
    env_var_key = rfs.CharField(required=True)
    required = rfs.BooleanField(required=True)

class CollectorSerializer(rfs.Serializer):

    CONFIG_FILE_NAME = "api_configuration.json"

    name = rfs.CharField(required=True)
    secrets = rfs.DictField(child=_SecretSerializer())


    @classmethod
    def _get_config_path(cls) -> str: 
           print(settings.PROJECT_DIR)
           return os.path.join(
                settings.PROJECT_DIR,"configuration",cls.CONFIG_FILE_NAME)
    
  
    def read_json_file(self)-> dict:
         config_path = self._get_config_path()
         with open(config_path) as f:
              config_dict = json.load(f)
         return config_dict
        
