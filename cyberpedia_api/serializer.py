from rest_framework import serializers as rfs
from data_collector.models import APIConfig

class APIConfigSerializer(rfs.ModelSerializer):
    class Meta:
        model = APIConfig
        fields = (
            "name",
            "type",
            "value",
            "required"
            "creation_date",
            "update_date",
        )

