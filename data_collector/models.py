from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core import serializers


class Feed(models.Model):

    name = models.TextField(_("name"),max_length=128)
    creation_date = models.DateTimeField(_("creation_date"),default=timezone.now)
   

    @staticmethod
    def collector_names():
        collector_list = Feed.objects.values('name').distinct().values('name')
        return collector_list

class APIConfig(models.Model):

    name = models.CharField(_('name'),max_length=126)
    value = models.TextField(_('value'),blank=True,null=False)
    required = models.BooleanField(_('required'))
    creation_date = models.DateTimeField(_("creation_date"),default = timezone.now)
    update_date = models.DateTimeField(_("update_date"),default= timezone.now)
    collector = models.ForeignKey(Feed, on_delete=models.CASCADE,null=True)

    @classmethod
    def to_json(cls):
        return serializers.serialize('json',APIConfig.objects.all())

    def update_key(self,value):
        self.value = value
        self.update_date = timezone.now()
        self.save(update_fields=["value","update_date"])

    
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
        indexes =  Index.objects.filter(collector = feed).values('name')
        if indexes.count() == 1:
            return indexes.get()
        return indexes

class DailyIndexMetadata(models.Model):

    index = models.ForeignKey(Feed,on_delete=models.CASCADE,null=False)
    timestamp = models.DateTimeField(auto_now_add=True,null=False)
    index_size = models.DecimalField(max_digits=5,decimal_places=5,default=0,null=False)    



    
