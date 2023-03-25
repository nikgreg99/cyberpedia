import uuid
from django.db import models
from django.utils import timezone
from djongo import  models  as djongo_models
from .constants import DataFeedFormat


class APIConfig(models.Model):
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    value = models.TextField(blank=True,null=False)
    required = models.BooleanField()
    creation_date = models.DateTimeField(default = timezone.now)
    update_date = models.DateTimeField(default= timezone.now)

    @staticmethod
    def collector_names():
        collector_list = APIConfig.objects.values('name').distinct()
        return collector_list

    
    def update_key(self,value):
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


    def update_feed(self, source, data: list):
        feed = DataFeed.objects.get(name = source)
        data_feed = DataFeedElement.objects.create(content= data)
        self.elements = self.elements + data_feed
        self.update_date = timezone.now()
        self.save(update_fields=['elements','update_time'])
    

    
