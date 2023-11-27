from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from accounts.api.serializers import UserSerializer, ProfileSerializer,UserdetailSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework import permissions
from .models import User, Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from rest_framework import status



class RegisterView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        Profile.objects.create(user=User.objects.last())
        return Response("user created successfully")

class LoginView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.get(email=email)
        if user.is_active:
            login(request,user)

        if not user.is_active:
            raise AuthenticationFailed('Account Inactive')

        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')
        
        serializer = UserSerializer(user)
        return Response('Logged in successfully')

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        logout(request)
        response = Response()
        response.data = {
            'message' : 'logout successful'
        }
        return response



class ProfileView(RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, pk):
        #get user with unique id
        user = User.objects.filter(id=pk).first()

        #get current logged in user id
        userloggedin = request.user

        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.is_active:
            raise AuthenticationFailed('Account Inactive')

        if not user.is_authenticated:
            raise AuthenticationFailed('Account unauthenticated')

        if userloggedin.id != user.id:
            raise AuthenticationFailed('Account unauthenticated')

        if user.is_authenticated:
            #check if user has a profile
            userprofile = Profile.objects.filter(user=user).last()

            serializer = ProfileSerializer(userprofile)    
        
            return Response(serializer.data)

        else:
            return Response("Not Authenticated")

class UserEditView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserdetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, pk):
        #get user with unique id
        user = User.objects.filter(id=pk).first()

        #compare loggedin user with current queried user
        userloggedin = request.user

        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.is_active:
            raise AuthenticationFailed('Account Inactive')

        if not user.is_authenticated:
            raise AuthenticationFailed('Account unauthenticated')

        if userloggedin.id != user.id:
            raise AuthenticationFailed('Account unauthenticated')

        if user.is_authenticated:
            serializer = UserdetailSerializer(user)    
            return Response(serializer.data)

        else:
            return Response("Not Authenticated")

        
        
        

