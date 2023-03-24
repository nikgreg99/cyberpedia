from django.shortcuts import render
from data_collector.models import DataFeed
from rest_framework import generics
# Create your views here.



class DataFeedList(generics.ListCreateAPIView):
    queryset = DataFeed.objects.all()
    serializer_class = DataFeed

