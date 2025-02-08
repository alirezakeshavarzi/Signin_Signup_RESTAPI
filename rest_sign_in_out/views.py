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



class Hello(APIView):
    permission_classes = (IsAuthenticated,)
    print('pemission : ////////////////////  ', permission_classes)

    def get(self, request):
        print('request : ///////////////////////////// : ', request)

        content = {'message' : 'HEllo , World! so i want to say this is message from jwt.!'}
        return Response(content)



@api_view(['GET','POST']) # this is first way to post info to databases.
def index(r):

    if r.method == 'POST':
        myusers = User(username = r.data['username'] , email = r.data['email'], password = r.data['password'])
        myusers.save()
        return Response("saved!")
    elif r.method == 'GET':
        myuser = User.objects.all()
        return Response(UserSerializers(myuser).data)



class PersonList(APIView):

    def get(self, r):
        # Use query_params to access query parameters
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

    def post(self, r):
        # For POST requests, r.data is correct
        username = r.data.get('username')
        email = r.data.get('email')
        password = r.data.get('password')

        if not username or not email or not password:
            return Response({"error": "Username, email, and password are required"}, status=400)

        myusers = User(username=username, email=email, password=password)
        myusers.save()
        return Response("Saved!")

class ChangePass(APIView):

    def post(self,request):
        request.data['lastpass']


# Create your views here.
