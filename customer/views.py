from django.shortcuts import render,redirect
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from clothesbackend import settings
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import redirect
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class CustomerViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = serializers.CustomerSerializer

class UserRegistrationApiView(APIView):
    serializer_class = serializers.RegestrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        print(request.data)
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            # customer = models.Customers(user=request.user,mobile_no=request.mobile_no,address=request.address)
            

            token = default_token_generator.make_token(user)
            print("token ",token)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print("uid ",uid)
            confirm_link = f"https://clothshopbackend-2.onrender.com/customer/active/{uid}/{token}"
            email_subject = "Account confirmation"
            email_body = render_to_string('confirm_email.html',{'confirm_link':confirm_link})
            email = EmailMultiAlternatives(email_subject,'',to=[user.email])
            email.attach_alternative(email_body,"text/html") 
            email.send()
            return Response("Check your email for confirmation!")
        return Response(serializer.errors)
    
def activate(request,uid64,token):
    try:
        uid = urlsafe_base64_decode(uid64).decode() 
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user=None
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        return HttpResponseRedirect(settings.FRONTEND_LOGIN_URL)
 
    else:
        return HttpResponseRedirect(settings.FRONTEND_REGISTER_URL)


class UserLogin(APIView):
    def post(self,request):
        serializer = serializers.UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username,password=password)

            if user:
                token,_ = Token.objects.get_or_create(user=user)
                print(token)
                print(_)
                login(request,user)
                return Response({'token':token.key, 'user_id':user.id})
            else:
                return Response({'error': "Invalid credentials."})
        return Response(serializer.errors)
    
class UserLogoutView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self,request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')
