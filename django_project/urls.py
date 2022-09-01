from django.urls import path,include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.contrib import admin
from pages.models import Musician,Issue,Sprint
from pages.serializers import MusicianSerializer, IssueSerializer, SprintSerializer, UserSerializer
from pages.views import MusicianView,IssueView,SprintView,UserView,temp_test
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = ['first_name', 'last_name', 'instrument']

urlpatterns = [
    path('admin/', admin.site.urls),
  
    path('mus/', MusicianView.as_view()),
    path('mus/<int:num>/', MusicianView.as_view()),

    path('jira/<int:num>/', IssueView.as_view()),
    path('jira/', IssueView.as_view()),

    path('jiraSprint/<int:num>/', SprintView.as_view()),
    path('jiraSprint/', SprintView.as_view()),

    path('users/', UserView.as_view()),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('temp/', temp_test ), 
]




