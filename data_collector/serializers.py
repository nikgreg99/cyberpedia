import os
import json
from rest_framework import serializers as rfs
from django.conf import settings
from .classes import Collector
from cache_memoize import cache_memoize
from .utils import compute_md5


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

    CONFIG_FILE_NAME = "api_configuration.json"

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
    def compute_md5_config_hash(cls):
          path = cls._get_config_path()
          with open(path,"r") as fp:
               content = fp.read().encode('utf-8')
               md5_hash = compute_md5(content)
          return md5_hash
    
    @classmethod
    @cache_memoize(
         timeout= 60 * 60 * 24 * 365,
         args_rewrite= lambda cls, user= None:  f"{cls.__name__}-"
         f"{cls.compute_md5_config_hash()}",
    ) 
    def read_and_verify_config(cls):
          return cls.read_json_file()
     