from djongo import models as djongo_models
from django.db import models
from django.utils import timezone
# Create your models here.


class DataFeedFormat(models.TextChoices):
    YARA = "Yara"
    STIX = "STIX"
    SIGMA = "SIGMA"
    SURICATA = "Suricata"
    OPEN_IOC = "Open_IOC"
    MISP = "MISP"
    OTHER = "Other"



class DataFeedElement(models.Model):

    id = models.UUIDField(primary_key=True)
    content = models.JSONField(blank=True)
    creation_date = models.DateTimeField(default=timezone.now)

class DataFeed(models.Model):

    #Constants
    DataFeedFormat = DataFeedFormat

    id = models.UUIDField(primary_key=True)
    source = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(blank=True,null=True)
    elements = djongo_models.ArrayField(model_container=DataFeedElement)

    def update(self,date):
        self.update_date = date
        self.save(update_fields=['update_date'])
