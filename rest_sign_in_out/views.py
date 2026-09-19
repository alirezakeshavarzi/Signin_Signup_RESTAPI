from tkinter import StringVar, Tk

from django.db.models.functions import window
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from rest_framework.decorators import api_view

from localStoragePy import localStoragePy

from .models import User

from .seri import UserSerializers


# this class (Hello) is only for testing the IsAuthenticated system and has no other purpose, i.e. if it IsAuthenticated, it prints the desired message.
class Hello(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        print('request : ///////////////////////////// : ', request)

        content = {'message' : 'Hello , World! so i want to say this is message from jwt.!'}
        return Response(content)



@api_view(['GET','POST']) # this is first way to post info to databases.
def index(req):

    # save info from user(that give it) to save in db.
    if req.method == 'POST':
        myusers = User(username = req.data['username'],
                       email = req.data['email'],
                       )

        myusers.set_password(req.data['password'])
        myusers.save()
        return Response("saved!")

    # get user info to show.
    elif req.method == 'GET':
        myuser = User.objects.all()
        return Response(UserSerializers(myuser, many=True).data)



class PersonList(APIView):
    permission_classes = [IsAuthenticated]  # Require authentication

    def get(self, r):
        username = r.query_params.get('username')
        password = r.query_params.get('password')

        if not username or not password:
            return Response({"error": "Username and password are required"}, status=400)

        my = User.objects.filter(username=username, password=password).values()
        my2 = UserSerializers(my, many=True)

        if my:
            return Response(my2.data)
        else:
            return Response({"error": "User not found"}, status=404)


# Create your views here.
