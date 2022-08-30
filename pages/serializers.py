
from rest_framework import routers, serializers, viewsets
from pages.models import Musician,Issue,Sprint
from django.contrib.auth import authenticate

class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = ['first_name', 'last_name', 'instrument','id']

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['type', 'description', 'status','id','sprint']

class SprintSerializer(serializers.ModelSerializer):
    issues = IssueSerializer(many=True)
    class Meta:
        model = Sprint
        fields = ['issues', 'name','id']


