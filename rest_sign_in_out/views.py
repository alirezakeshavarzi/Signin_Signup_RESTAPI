
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from rest_framework.decorators import api_view


from .models import User

from .seri import UserSerializers


# this class (Hello) is only for testing the IsAuthenticated system and has no other purpose, i.e. if it IsAuthenticated, it prints the desired message.
class Hello(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):

        content = {'message' : 'Hello , World! so i want to say this is message from jwt.!'}
        return Response(content)




class Rigister(APIView):

    def post(self, req):
        # save info from user(that give it) to save in db.
        myusers = User(username = req.data['username'],
                       email = req.data['email'],
                       )

        myusers.set_password(req.data['password'])
        myusers.save()
        return Response("saved!")


# display information about the user logged into their account
class UserInfo(APIView):
    permission_classes = [IsAuthenticated]  # Require authentication

    def get(self, req):

        my_serializer = UserSerializers(req.user)
        return Response(my_serializer.data)


# Create your views here.
