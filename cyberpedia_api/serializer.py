from rest_framework import serializers as rfs
from data_collector.models import DataFeed

class DataFeedSerializer(rfs.ModelSerializer):
    class Meta:
        model = DataFeed
        fields = (
            "feed_id",
            "name",
            "creation_date",
            "update_date",
            "type",
            "elements"
        )

