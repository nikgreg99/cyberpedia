import uuid
from django.db import models
from django.utils import timezone
from djongo import  models  as djongo_models
from .constants import DataFeedFormat

class APIConfig(models.Model):
    config_id = models.UUIDField(auto_created=True,unique=True,default=uuid.uuid4)
    name = models.TextField(max_length=128)
    type = models.TextField(max_length=128)
    value = models.TextField(max_length=128, blank=True)
    required = models.BooleanField()
    creation_date = models.DateTimeField(default = timezone.now)
    update_date = models.DateTimeField(blank=True)

    @staticmethod
    def collector_names():
        collector_list = APIConfig.objects.values('name').distinct()
        return collector_list

    
    def update_apikey_date(self,value):
        self.value = value
        self.update_date = timezone.now()
        self.save(update_fields=["update_date"])


class DataFeedElement(models.Model):

    class Meta:
        abstract = True

    element_id = models.UUIDField(unique=True,auto_created=True, default=uuid.uuid4)
    content = models.JSONField(blank=True)
    creation_date = models.DateTimeField(default=timezone.now)
   

class DataFeed(models.Model):

    #Constants
    DataFeedFormat = DataFeedFormat
    feed_id = models.UUIDField(unique=True,auto_created=True,default=uuid.uuid4)
    name = models.TextField(blank=False)
    creation_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(blank=True,null=True)
    format_type = models.CharField(max_length=128, choices=DataFeedFormat.choices,default=DataFeedFormat.OTHER)
    elements = djongo_models.ArrayField(model_container=DataFeedElement)


    def update_feed(self,data: list):
        if data is not None:
            for data_block in data:
                self.elemen
    

    
