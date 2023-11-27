from django.contrib import admin
from django.urls import path, include
from .views import RegisterView, ProfileView, LoginView, LogoutView, UserEditView

urlpatterns = [
    path('accounts/register/', RegisterView.as_view()),
    path('accounts/login/', LoginView.as_view()),
    path('accounts/logout/', LogoutView.as_view()),
    path('accounts/profile/<int:pk>', ProfileView.as_view()),
    path('accounts/edituser/<int:pk>', UserEditView.as_view()),
]

