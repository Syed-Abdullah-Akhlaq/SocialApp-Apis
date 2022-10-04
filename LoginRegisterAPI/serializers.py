from rest_framework import  serializers
from randomApplication.models import User


class userSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length = 65, min_length = 8, write_only = True)
    email = serializers.EmailField(max_length = 255, min_length = 4)
    first_name = serializers.CharField(max_length = 255, min_length = 2)
    last_name = serializers.CharField(max_length = 255, min_length = 2)

    
    class Meta:
        model = User
        fields = ['id','username', 'first_name', 'last_name', 'email', 'password']


    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError(('Email is already in use',email))
        return super().validate(attrs)


    def create(self, validated_data):
        user =User.objects.create_user(**validated_data)
        user.is_active =False
        user.save()
        return user
        



class loginSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length = 65, min_length = 8, write_only = True)
    username = serializers.CharField(max_length = 255, min_length = 2)

    class Meta:
        model = User
        fields = ['username', 'password']

