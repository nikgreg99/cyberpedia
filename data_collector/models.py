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


class DataFeed(models.Model):

    #Constants
    DataFeedFormat = DataFeedFormat

    name = models.TextField(max_length=100)
    feed_format = models.TextField(choices=DataFeedFormat.choices,primary_key=True)
    description = models.TextField(null=True)
    feed_data_creation = models.DateTimeField(default=timezone.now())


class DataFeedItem(models.Model):
    uuid = models.UUIDField(primary_key=True)
    report = models.JSONField(default=dict)
    creation_date = models.DateTimeField(default=timezone.now())
    data_feed = models.ForeignKey(DataFeed, on_delete=models.CASCADE)
