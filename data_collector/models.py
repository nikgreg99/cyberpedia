from django.db import models
from django.utils import timezone


class DataFeedFormat(models.TextChoices):
    YARA = "Yara"
    STIX = "STIX"
    SIGMA = "SIGMA"
    SURICATA = "Suricata"
    OPEN_IOC = "Open_IOC"
    MISP = "MISP"
    OTHER = "Other"



class DataCollectorSecret(models.Model):
    name = models.TextField()
    value = models.TextField()
    required = models.BooleanField()

class DataCollector(models.Model):

    #Constants
    DataFeedFormat = DataFeedFormat
    name = models.TextField()
    data_feed_type = models.TextField(choices=DataFeedFormat.choices,primary_key=True)
    secrets = models.ManyToManyField(DataCollectorSecret)


class DataFeed(models.Model):

    name = models.TextField(max_length=100)
    description = models.TextField(null=True)
    feed_data_creation = models.DateTimeField(default=timezone.now())
    collector = models.ForeignKey(DataCollector,on_delete= models.CASCADE)

class DataFeedItem(models.Model):
    uuid = models.UUIDField(primary_key=True)
    report = models.JSONField(default=dict)
    creation_date = models.DateTimeField(default=timezone.now())
    data_feed = models.ForeignKey(DataFeed, on_delete=models.CASCADE)
