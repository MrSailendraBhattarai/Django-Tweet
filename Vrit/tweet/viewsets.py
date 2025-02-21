from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import tweetSerializer
from .models import Tweet

class tweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = tweetSerializer