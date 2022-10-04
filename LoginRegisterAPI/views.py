# from os import SCHED_BATCH
from rest_framework.generics import GenericAPIView
from randomApplication.models import User
from .serializers import userSerializer,loginSerializer
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib import auth
import jwt
from rest_framework_simplejwt.tokens import RefreshToken
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from rest_framework import generics
from django.conf import settings
# Create your views here.

class registerView(GenericAPIView):
    serializer_class = userSerializer
    def post(self,request, *args, **kwargs):
        serializer = userSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            user_data = serializer.data
            user = User.objects.get(email = user_data['email'])
            token = RefreshToken.for_user(user).access_token

            current_site = get_current_site(request).domain
            relativeLink = reverse ('email-verify')
            absurl = 'http://'+ current_site + relativeLink + "?token=" +str(token)
            email_body = 'Hi' + user.username +'Use link below to verify your email \n' + absurl
            data = {'email_body': email_body,'from_email':"abdullahakhlaq14@gmail.com", 'to_email': user.email, 'email_subject': 'verify your email'}
            Util.send_email(data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyEmail(generics.GenericAPIView):
        def get(self, request):
            token = request.GET.get('token')
            print('get',token)
            try:
                payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
                print(payload,'payload')
                user = User.objects.get(id=payload['user_id'])
                print('user:',user)
                if not user.is_active:
                    print("-------------")
                    user.is_active = True
                    user.save()
                    return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
            except jwt.ExpiredSignatureError as identifier:
                return Response({'error': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
            except jwt.exceptions.DecodeError as identifier:
                return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)





class loginView(GenericAPIView):
    serializer_class = loginSerializer
    def post(self,request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth_token = jwt.encode({'username':user.username},settings.JWT_SECRET_KEY, algorithm="HS256")
            print("---------",settings.JWT_SECRET_KEY)
            serializer = userSerializer(user)
            data = {'user': serializer.data,'token': auth_token}
            return Response(data, status=status.HTTP_200_OK)

        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)







        