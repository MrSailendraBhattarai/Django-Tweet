from rest_framework import serializers
from django.contrib.auth.models import User
from . models import Tweet

class tweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = '__all__'