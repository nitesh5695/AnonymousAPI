
import jwt
import datetime
import requests
import json
from django.conf import settings
from rest_framework import authentication
from .models import anonymousUser,customer_model
from .serializers import customer_serializer,RegisterSerializer
from .JwtTokens import access_token,refresh_token
from rest_framework.views import APIView
from rest_framework import exceptions
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication 
from .customauth import AnonymousJWTAuthentication
from .custompermission import AnonymousPermission
# Create your views here.
class token_anonymous(APIView):
    
    def post(self,request):
        
        
        ip=request.META.get('REMOTE_ADDR')
        
        userip=str(ip)
        try:
            user=anonymousUser.objects.get(username=userip)
            token=access_token(user)
            refresh=refresh_token(user)
            current_user=str(request.user)
           
             
        except anonymousUser.DoesNotExist:
            newuser=anonymousUser(username=userip)  
            newuser.save()  
            
            user=anonymousUser.objects.get(username=userip)
           
            token=access_token(user)
            refresh=refresh_token(user)
            current_user=str(request.user)
           
           
        return Response({"user":current_user,
            'access':str(token),
            'Refresh':str(refresh)
            })
       
class RefreshTokenAnonymous(APIView):
    def post(self,request):
        R_token=request.data.get('refresh')
        if R_token is not None:
            try:
                payload=jwt.decode(R_token,settings.SECRET_KEY,algorithms=['HS256'])
                username=payload['username']
                token_payload={
                    'username':username,
                    'exp':datetime.datetime.utcnow() + datetime.timedelta(days=0,minutes=15),
                    'iat':datetime.datetime.utcnow(),
                }
                access_token=jwt.encode(token_payload,settings.SECRET_KEY,algorithm='HS256')
                return Response({"access_token":str(access_token)})
            except jwt.DecodeError as identifier:
                raise exceptions.AuthenticationFailed('your token is invalid')
            except jwt.ExpiredSignatureError as identifier:
                raise exceptions.AuthenticationFailed('token is expired')  

class access(APIView):
   authentication_classes=[AnonymousJWTAuthentication] 
   permission_classes=[AnonymousPermission]
   def post(self,request):
       
       return Response({'message':'post method working'})
   def get(self,request):
        all_customer=customer_model.objects.all()
        Serializer=customer_serializer(all_customer,many=True)
        
        return Response(Serializer.data)   

# Create your views here.
class register(APIView):
    authentication_classes=[AnonymousJWTAuthentication] 
    def post(self,request):
        json_data=request.data
        captcha_detail=json_data.get('captcha')
        url= "https://www.google.com/recaptcha/api/siteverify"
        response_data=requests.post(url,data=captcha_detail)
        response=json.loads(response_data.text)
        verify=response['success']
        print(verify)
        if verify:
            gst_no=json_data.get('gst_no')
            if gst_no is not None:
                """create logic to validate gst no"""
                gst_valid=True
                pass
            else:
                return Response({"message":"please provide valid gst_no"})
            if gst_valid==True:   
                serializer=RegisterSerializer(data=request.data ,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"message":"registered"})
                else:
                    return Response(serializer.errors)    
        else:
            return Response({"message":"captcha error"})            
class customers(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        
        all_customer=customer_model.objects.all()
        Serializer=customer_serializer(all_customer,many=True)
        
        return Response(Serializer.data)

    def post(self,request):
        Serializer=customer_serializer(data=request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response({"mesage":"succcesfully added"})   
        else:
            return Response(Serializer.errors)  

     
    def patch(self,request):    
        json_data=request.data
        
        id=json_data.get("id")
        
        if id is not None:
            customer_data=customer_model.objects.get(id=id)
            Serializer=customer_serializer(customer_data,data=json_data) 
            if Serializer.is_valid():
                Serializer.save()
                return Response({"message":"updated"})
            else:
                return Response(Serializer.errors)
        return Response({"message":"id sholud be given"})
