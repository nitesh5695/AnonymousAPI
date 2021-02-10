from requests.models import DecodeError
from rest_framework import authentication
from rest_framework.authentication import BaseAuthentication
from .models import anonymousUser
from rest_framework import exceptions
import jwt
from django.conf import settings
from django.contrib.auth.models import User


class AnonymousJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_data=authentication.get_authorization_header(request)
        if not auth_data:
            raise exceptions.AuthenticationFailed('please provide token')
        try:  
          prefix,token =auth_data.decode('utf-8').split(' ')
          print(prefix)
          if prefix != "Bearer":
            raise exceptions.AuthenticationFailed('invalid token prefix')

        except DecodeError:
           raise exceptions.AuthenticationFailed('please provide token with prefix')
        try:
        
          payload=jwt.decode(token,settings.SECRET_KEY,algorithms=['HS256'])
          
          username=payload['username']
          print(payload)
          user =anonymousUser.objects.get(username=username)
          
          request.session['username']=user.username
          #print(request.user)
          print(user)
          return (user,token)
        except anonymousUser.DoesNotExist:
          payload=jwt.decode(token,settings.SECRET_KEY,algorithms=['HS256'])
          print(payload)
          username=payload['username']
         
          user =User.objects.get(username=username)
         
          request.session['username']=user.username
          print("register user")
          return (user,token)  
        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed('your token is invalid')
        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed('token is expired')
        
            
