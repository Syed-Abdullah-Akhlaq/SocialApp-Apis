from operator import truediv
from django.db import models
# from django.contrib.auth.models import User
from randomApplication.models import User
# Create your models here.

class CRUD(models.Model):
    owner = models.ForeignKey(to = User, on_delete=models.CASCADE)
    country_code = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    contact_picture = models.URLField(null=True)
    is_favorite = models.BooleanField(default=True)



class Post(models.Model):
    post = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'posts')


class LikePost(models.Model):
    like = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'likes')
    userLike = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'UserLike', null = True)


class CommentPost(models.Model):
    comment = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'comments')
    userComment = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'UserComment', null = True)
