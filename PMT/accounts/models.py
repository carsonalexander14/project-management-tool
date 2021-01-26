from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import PermissionsMixin


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, username, display_name=None, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not display_name:
            display_name = username
            
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            display_name=display_name
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, username, display_name, password):

        user = self.create_user(
            email,
            username,
            display_name,
            password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=15, unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    display_name = models.CharField(max_length=25, default="")
    avatar = models.ImageField(upload_to='profile_avatar', blank=True, default="default_avatar.png")
    bio = models.CharField(max_length=140, blank=True, default="")
    skills = models.ManyToManyField('Skill', related_name="users")
    
    objects = UserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["display_name", "username"]
    
    def __str__(self):
        return "@{}".format(self.username)
    
    def get_short_name(self):
        return self.display_name
    
    def get_long_name(self):
        return "{} (@{})".format(self.display_name, self.username)


class Skill(models.Model):
    title = models.CharField(max_length=15)

    def __str__(self):
        return self.title
        