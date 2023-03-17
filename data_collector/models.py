from django.db import models
from django.utils import timezone

class APIConfig(models.Model):
    collector_name = models.TextField(max_length=128)
    type = models.TextField(max_length=128)
    value = models.TextField(max_length=128)
    required = models.BooleanField()
    creation_date = models.DateTimeField(default = timezone.now)
    update_date = models.DateTimeField(blank=True)

    @staticmethod
    def collector_names():
        collector_list = APIConfig.objects.values('collector_name').distinct()
        return collector_list

    
    def update_key(self,value):
        self.value = value
        self.update_date = timezone.now()
        self.save(update_fields=["update_date"])







    




class DataFeed(models.Model):

    name = models.TextField(max_length=100)
    description = models.TextField(null=True,blank=True)
    feed_data_creation = models.DateTimeField(default=timezone.now())

class DataFeedItem(models.Model):
    uuid = models.UUIDField(primary_key=True)
    report = models.JSONField(default=dict)
    creation_date = models.DateTimeField(default=timezone.now())
    data_feed = models.ForeignKey(DataFeed, on_delete=models.CASCADE)
