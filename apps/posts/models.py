from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField(max_length=512)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    liked_by = models.ManyToManyField(User, through='Like', related_name='posts_liked')


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


def get_sample(limit=10):
    return Post.objects.all()[:limit]
