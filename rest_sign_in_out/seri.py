from rest_framework import serializers

from .models import User

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'fname', 'lname', 'username', 'email', 'phone','password']