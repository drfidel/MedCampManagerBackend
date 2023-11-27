from django.contrib import admin
from .models import User, Profile
from django.contrib.auth.admin import UserAdmin


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo', 'department']


admin.site.register(User, UserAdmin)