from rest_framework import serializers
from randomApplication.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ['id','username','friends', 'blockList','from_user', 'to_user','fromBlock','toBlock']


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)
