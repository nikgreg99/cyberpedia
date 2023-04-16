from django.shortcuts import render
from data_collector.models import APIConfig
from .serializer import APIConfigSerializer
from rest_framework import generics
# Create your views here.

generics.RetrieveAPIView
class APIConfigList(generics.ListCreateAPIView):
    queryset = APIConfig.objects.all()
    serializer_class = APIConfigSerializer

