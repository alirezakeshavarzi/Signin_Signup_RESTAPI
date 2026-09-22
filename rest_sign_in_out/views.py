
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from .seri import UserRegisterSerializer, UserInfoSerializer


# just for test
class Hello(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):

        content = {'message': 'Hello , World!'}
        return Response(content)




class Rigister(APIView):

    def post(self, req):

        ser = UserRegisterSerializer(data=req.data)

        if ser.is_valid():
            ser.save()
            return Response("saved!")

        return Response(ser.errors, status=400)


# display information about the user logged into their account
class UserInfo(APIView):
    permission_classes = [IsAuthenticated]  # Require authentication

    def get(self, req):

        my_serializer = UserInfoSerializer(req.user)
        return Response(my_serializer.data)


# Create your views here.
