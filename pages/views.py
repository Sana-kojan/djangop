from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from pages.models import Musician,Issue
from pages.serializers import MusicianSerializer, IssueSerializer
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
        user.first_name  = request.data["first_name"]
        user.last_name  = request.data["last_name"]
        user.instrument  = request.data["instrument"]
        user.save()
        return Response(MusicianSerializer(user).data)

    def delete(self,request,num):
        user = Musician.objects.get(id=num)
        user.delete()
        return Response()



class IssueView(APIView):
    def get(self, request,num=None):
        return Response(IssueSerializer(Issue.objects.all(),many=True).data)

    def post(self,request,num=None):
        issueJ =IssueSerializer(Issue.objects.create(
            type=request.data["type"],
            description=request.data["description"],
            status=request.data["status"])).data
        return Response(issueJ)

    def patch(self,request,num=None):
        issueJ = Issue.objects.get(id=request.data["id"])
        print(request.data)
        setattr(issueJ,request.data["key"],request.data["value"])
        issueJ.save()
        return Response(IssueSerializer(issueJ).data)

    def delete(self,request,num):
        issueJ = Issue.objects.get(id=num)
        issueJ.delete()
        return Response()
       
            