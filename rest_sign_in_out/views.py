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

#first way to post in the ORM(database)
@api_view(['GET', 'POST'])
def index(r):
    p = User.objects.get(id=2)
    se = UserSerializers(p)

    print('////////////////////// : ', se.data)
    return Response({"Hello workd"})

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
