from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager


class Users(AbstractUser):
    profile_pic = models.CharField(max_length=30, null=True)
    last_activity = models.DateTimeField(null=True,blank=True)
   
    class Meta(AbstractUser.Meta):
        swappable = 'user_profiles'
