from django.urls import path,include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.contrib import admin
from pages.models import Musician,Issue
from pages.views import MusicianView,IssueView

class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = ['first_name', 'last_name', 'instrument']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = ['first_name', 'last_name', 'instrument']

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['type', 'description', 'status','id']


class UserViewSet(viewsets.ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = UserSerializer


router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
  
    path('mus/', MusicianView.as_view()),
    path('mus/<int:num>/', MusicianView.as_view()),

    path('jira/<int:num>/', IssueView.as_view()),
    path('jira/', IssueView.as_view()),
]




