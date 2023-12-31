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
from django.db import models
from django.contrib.auth.models import AbstractUser,User
from django.utils.text import slugify
    
class User(AbstractUser):
    email = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True, default="")
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = slugify(self.email)
        super().save(*args, **kwargs)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


class Profile(models.Model):
    user = models.OneToOneField(User,related_name="user", on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',blank=True)
    profession = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)
    contact = models.CharField(max_length=13, blank=True)
    role = models.CharField(max_length=20, default="NURSE")

    @property
    def username(self):
        return self.user.username

    def __str__(self):
        return f'Profile for user {self.user.username}'
