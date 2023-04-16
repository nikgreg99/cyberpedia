from django.urls import include,path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import APIConfigList

urlpatterns = [
    path("/sources/configuration",APIConfigList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)