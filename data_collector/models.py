import uuid
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from djongo import models as djongo_models


class APIConfig(models.Model):
    name = models.CharField(_('name'), max_length=128)
    type = models.CharField(_('type'),max_length=128)
    value = models.TextField(_('value'),blank=True,null=False)
    required = models.BooleanField(_('required'))
    creation_date = models.DateTimeField(_("creation_date"),default = timezone.now)
    update_date = models.DateTimeField(_("update_date"),default= timezone.now)


    def update_key(self,value):
        self.value = value
        self.update_date = timezone.now()
        self.save(update_fields=["update_date"])

class FeedElement(djongo_models.Model):

    class Meta:
        abstract = True

    creation_date = djongo_models.DateTimeField(_("creation_date"), auto_now=False, auto_now_add=False)
    content = djongo_models.TextField(_("content"))
   

class DataFeed(models.Model):


    name = models.TextField(_("name"),max_length=128)
    creation_date = models.DateTimeField(_("creation_date"),default=timezone.now)
    update_date = models.DateTimeField(_("update_date"),blank=True,null=True)
    elements = djongo_models.ArrayField(model_container=FeedElement)

    objects = djongo_models.DjongoManager()

    @staticmethod
    def collector_names():
        collector_list = DataFeed.objects.values('name').distinct()
        return collector_list
    



    
