
from rest_framework import routers, serializers, viewsets
from pages.models import Musician,Issue


class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = ['first_name', 'last_name', 'instrument','id']

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['type', 'description', 'status','id']