
from rest_framework import routers, serializers, viewsets
from pages.models import Musician,Issue,Sprint
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class UserSerializer2(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'id',]

class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = ['first_name', 'last_name', 'instrument','id']

class IssueSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    class Meta:
        model = Issue
        fields = ['type', 'description', 'status','id','sprint','user',"username"]
    
    def get_username(self,obj):
        print(self.context)
        if(obj.user_id):
            return obj.user.username
        return None

class UserSerializer(serializers.ModelSerializer):
    issues = IssueSerializer(many=True)
    class Meta:
        model = User
        fields = ['username', 'id','issues']

class SprintSerializer(serializers.ModelSerializer):
    issues = IssueSerializer(many=True)
    class Meta:
        model = Sprint
        fields = ['issues', 'name','id']
        