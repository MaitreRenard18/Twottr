from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    display_name = models.CharField(max_length=50, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True, default='media/profile_pictures/default.jpg')
    banner = models.ImageField(upload_to='banners/', blank=True, null=True, default='media/banners/default.jpg')
    bio = models.TextField(blank=True, null=True, max_length=500)

    liked_posts = models.ManyToManyField('posts.Post', through='posts.Like', related_name='users_liked')  # Changement ici


def get_user_from_username(username: str) -> User:
    return User.objects.get(username=username)
