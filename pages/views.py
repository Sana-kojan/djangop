from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from pages.models import Musician,Issue,Sprint
from pages.serializers import MusicianSerializer, IssueSerializer, SprintSerializer
from rest_framework.permissions import IsAuthenticated
def homePageView(request):
    return HttpResponse("Hello, World!")

class MusicianView(APIView):
    def get(self, request,num=None):
        return Response(MusicianSerializer(Musician.objects.all(),many=True).data)
    def post(self,request,num=None):
        user =MusicianSerializer(Musician.objects.create(first_name=request.data["first_name"],last_name=request.data["last_name"],instrument=request.data["instrument"])).data
        return Response(user)

    def patch(self,request,num=None):
        user = Musician.objects.get(id=request.data["id"])
        user.first_name  = request.data.get("first_name")
        user.last_name  = request.data.get("last_name")
        user.instrument  = request.data.get("instrument")
        user.save()
        return Response(MusicianSerializer(user).data)

    def delete(self,request,num):
        user = Musician.objects.get(id=num)
        user.delete()
        return Response()



class IssueView(APIView):
    def get(self, request,num=None):
        print(request.user)
        return Response(IssueSerializer(Issue.objects.filter(sprint__isnull=True),many=True).data)

    def post(self,request,num=None):
        print(request.data)
        issueJ =IssueSerializer(Issue.objects.create(
            type=request.data.get("type"),
            description=request.data.get("description"),
            status=request.data.get("status"),
            sprint_id=request.data.get("sprint"))).data
        return Response(issueJ)

    def patch(self,request,num=None):
        issueJ = Issue.objects.get(id=request.data.get("id"))
        print(request.data)
        setattr(issueJ,request.data.get("key"),request.data.get("value"))
        issueJ.save()
        return Response(IssueSerializer(issueJ).data)

    def delete(self,request,num):
        issueJ = Issue.objects.get(id=num)
        issueJ.delete()
        return Response()

class SprintView(APIView):
    def get(self, request ,num=None):
        return Response(SprintSerializer(Sprint.objects.all(),many=True).data)

    def post(self,request,num=None):
        sprints =SprintSerializer(Sprint.objects.create(
            name=request.data.get("name"),
         )).data
        return Response(sprints)

    def patch(self,request,num=None):
        sprints = Sprint.objects.get(id=request.data.get("id"))
        setattr(issueJ,request.data.get("key"),request.data.get("value"))
        sprints.save()
        return Response(SprintSerializer(sprints).data)

    def delete(self,request,num):
        sprints = Sprint.objects.get(id=num)
        sprints.delete()
        return Response()
       
            