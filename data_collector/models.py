from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core import serializers

class APIConfig(models.Model):
    name = models.CharField(_('name'), max_length=128)
    type = models.CharField(_('type'),max_length=128)
    value = models.TextField(_('value'),blank=True,null=False)
    required = models.BooleanField(_('required'))
    creation_date = models.DateTimeField(_("creation_date"),default = timezone.now)
    update_date = models.DateTimeField(_("update_date"),default= timezone.now)

    @classmethod
    def to_json(cls):
        return serializers.serialize('json',APIConfig.objects.all())

    def update_key(self,value):
        self.value = value
        self.update_date = timezone.now()
        self.save(update_fields=["value","update_date"])

class Feed(models.Model):

    name = models.TextField(_("name"),max_length=128)
    creation_date = models.DateTimeField(_("creation_date"),default=timezone.now)

    @staticmethod
    def collector_names():
        collector_list = Feed.objects.values('name').distinct()
        return collector_list
    
class Index(models.Model):
    
    name = models.TextField(_("name"),max_length=128)
    collector = models.ForeignKey(Feed,on_delete=models.CASCADE, null=True)

    @staticmethod
    def indexes():
        indexes = Index.objects.values('name').distinct()
        return indexes
    
    @staticmethod
    def indexes_by_key(collector_name):
        feed = Feed.objects.get(name=collector_name)
        return Index.objects.filter(collector = feed.id).values('name')
    



    
