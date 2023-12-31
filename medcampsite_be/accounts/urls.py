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

    Django settings for medcampsite_be project.

    Generated by 'django-admin startproject' using Django 4.2.7.

"""
from django.contrib import admin
from django.urls import path, include
from .views import RegisterView, ProfileView, LoginView, LogoutView, UserEditView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('profile/<int:pk>', ProfileView.as_view()),
    path('user/<int:pk>', UserEditView.as_view()),
    path('password/reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('password/reset/confirm/', include('django_rest_passwordreset.urls', namespace='password_reset_confirm')),

]

