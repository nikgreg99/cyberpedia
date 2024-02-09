import os
import json
from rest_framework import serializers as rfs
from django.conf import settings
from .classes import Collector
from cache_memoize import cache_memoize



class _SecretSerializer(rfs.Serializer):
    env_var_key = rfs.CharField(required=True)
    required = rfs.BooleanField(required=True)

class _ParamSerializer(rfs.Serializer):
     name: rfs.CharField(required=True)
     type: rfs.CharField(required=True)
     description: rfs.CharField(required=True)


class CollectorSerializer(rfs.ModelSerializer):
    
    class Meta:
         model = Collector
         fields = "__all__"

    CONFIG_FILE_NAME = "config.json"

    name = rfs.CharField(required=True)
    secrets = rfs.DictField(child=_SecretSerializer())
    parameters = rfs.DictField(child=_ParamSerializer())

    def validate(self, attrs):
         return super().validate(attrs)


    @classmethod
    def _get_config_path(cls) -> str: 
           return os.path.join(
                settings.PROJECT_DIR,"configuration",cls.CONFIG_FILE_NAME)
    
    @classmethod
    def read_json_file(cls)-> dict:
         config_path = cls._get_config_path()
         with open(config_path) as f:
              config_dict = json.load(f)
         return config_dict
    
    
    @classmethod
    @cache_memoize(
         timeout= 60 * 60 * 24 * 365
    ) 
    def read_and_verify_config(cls):
          return cls.read_json_file()
     