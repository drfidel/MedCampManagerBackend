"""
    Copyright (C) <2023>  <Dr. Akiyo Fidel>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>

"""
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from accounts.api.serializers import UserSerializer, ProfileSerializer,UserdetailSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework import permissions
from .models import User, Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token


class RegisterView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @method_decorator(csrf_exempt)
    def post(self, request):
        serializer = UserSerializer(data=request.data)    
        serializer.is_valid(raise_exception=True)
        serializer.save()

        token = Token.objects.create(user=User.objects.last())
        
        Profile.objects.create(user=User.objects.last())
        return Response({'token':str(token)},status=201)

class LoginView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @method_decorator(csrf_exempt)
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = get_object_or_404(User, email=email)
            
        if not user.is_active:
            raise AuthenticationFailed('Account Inactive')

        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')
        if user is not None:
            login(request,user)
            try:
                token = Token.objects.get(user=user)
            except: # if token not in db, create a new one
                token = Token.objects.create(user=user)
        
        serializer = UserSerializer(user)
        return Response({'token':str(token)},status=201)

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @method_decorator(csrf_exempt)
    def post(self, request):
        logout(request)
        response = Response()
        response.data = {
            'message' : 'logout successful'
        }
        return response

class ProfileView(APIView):
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
            #check if user has a profile WITH GIVEN_ID 8
            userprofile = ProfileView.queryset.get(user=pk)
            
            editprofile = Profile.objects.filter(user=user).first()
            serializer = ProfileSerializer(editprofile)    
        
            return Response(serializer.data)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        #check if user has a profile WITH GIVEN_ID 8
        userprofile = ProfileView.queryset.get(user=pk)


        serializer = ProfileSerializer(userprofile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)


class UserEditView(APIView):
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

        return Response("Not Authenticated")

    def put(self, request, pk):
        useredit = UserEditView.queryset.get(id=pk)


        serializer = UserdetailSerializer(useredit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)

        
        
        

