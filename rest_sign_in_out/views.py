from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from rest_framework.decorators import api_view

from .models import User





from .seri import UserSerializers


class HelloWorld(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, requ):
        content = {'message' : 'HEllo , World! so i want to say this is message from jwt.!'}
        return Response(content)

@api_view(['GET','POST']) # this is first way to post info to databases.
def index(r):

    if r.method == 'POST':
        myusers = User(username = r.data['username'] , email = r.data['email'], password = r.data['password'])
        myusers.save()
        return Response("saved!")
    else:
        return Response('please try with post.')


class PersonList(APIView):

    def get(self, r):
        my = User.objects.all().values()

        print('This is my : ////////////' )

        my2 = UserSerializers(my, many=True)
        return Response(my2.data)
    def post(self, r):
        return Response(r.data)

    def delete(self,r):
        return Response(r.data)
# Create your views here.
