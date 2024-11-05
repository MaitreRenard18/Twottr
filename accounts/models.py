from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True, default='profile_pictures/default.jpg')
    bio = models.TextField(blank=True, null=True, max_length=500)


def get_user_from_username(username: str) -> User:
    return User.objects.get(username=username)
