import uuid
from django.db import models
from django.utils import timezone
from djongo import  models  as djongo_models
from django.utils.translation import ugettext_lazy as _
from .constants import DataFeedFormat


class APIConfig(models.Model):
    name = models.CharField(_('name'), max_length=128, )
    type = models.CharField(_('type'),max_length=128)
    value = models.TextField(_('value'),blank=True,null=False)
    required = models.BooleanField(_('required'))
    creation_date = models.DateTimeField(_("creation_date"),default = timezone.now)
    update_date = models.DateTimeField(_("update_date"),default= timezone.now)


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
    name = models.TextField(blank=False)
    creation_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(blank=True,null=True)
    elements = models.JSONField()

    objects = djongo_models.DjongoManager()

    @staticmethod
    def collector_names():
        collector_list = DataFeed.objects.values('name').distinct()
        return collector_list

    
