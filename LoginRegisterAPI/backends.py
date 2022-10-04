import jwt
from rest_framework import authentication,exceptions
from django.conf import settings
# from django.contrib.auth.models import User
from randomApplication.models import User


class JWTauthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)
        if not auth_data:
            return None
        print("auth_data", auth_data)
        prefix,token = auth_data.decode('utf-8').split(" ")
        print(token)

        try:
            payload  = jwt.decode(token,settings.JWT_SECRET_KEY, algorithms="HS256")
            print('payload', payload)
            user = User.objects.get(username=payload['username'])
            print('user', user)
            return (user, token)
            

        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed('Your token is invalid,login')


        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed('Your token is expired,login')


        return super().authenticate(request)