from asyncore import read
from rest_framework.serializers import ModelSerializer
from .models import CRUD,Post,LikePost,CommentPost
from django.db import connection

class CRUDserializer(ModelSerializer):
    class Meta:
            model = CRUD
            fields = ['id','owner','country_code', 'first_name', 'last_name', 'phone_number', 'contact_picture', 'is_favorite']



class PostLikeSeializer(ModelSerializer):
    # likes = PostSerializer(many=True,read_only=True)
    class Meta:
        model = LikePost
        fields = ['id','like', 'userLike']

class PostCommentSeializer(ModelSerializer):
    # comments = PostSerializer(many=True,read_only=True)
    class Meta:
        model = CommentPost
        fields = ['id','comment', 'userComment']

class PostSerializer(ModelSerializer):
    likes = PostLikeSeializer(many = True, read_only = True)
    comments = PostCommentSeializer(many = True, read_only = True)
    @staticmethod
    def setup_eager_loading(queryset):
        """ Perform necessary eager loading of data. """

        queryset=queryset
        for i in queryset:
            print(i.likes.all())
            print(i.comments.all())
        # print(queryset)
        # print('sql:',len(connection.queries))
        return queryset
    class Meta:
        model = Post
        fields = ['id','post', 'likes', 'comments']

