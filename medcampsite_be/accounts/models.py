from django.db import models
from django.contrib.auth.models import AbstractUser,User
    
class User(AbstractUser):
    email = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True, default="")
    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',blank=True)
    profession = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'
