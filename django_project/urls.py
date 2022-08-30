from django.urls import path,include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.contrib import admin
from pages.models import Musician,Issue,Sprint
from pages.serializers import MusicianSerializer, IssueSerializer, SprintSerializer
from pages.views import MusicianView,IssueView,SprintView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = ['first_name', 'last_name', 'instrument']




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

    path('jiraSprint/<int:num>/', SprintView.as_view()),
    path('jiraSprint/', SprintView.as_view()),

 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]




