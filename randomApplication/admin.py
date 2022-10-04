import imp
from django.contrib import admin
from CRUD .models import Post, LikePost , CommentPost
from randomApplication.models import FriendRequest, User, blockList

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display= ['id','username']

@admin.register(FriendRequest)
class FriendAdmin(admin.ModelAdmin):
    list_display = [
        "id", "from_user","to_user"
    ]


@admin.register(blockList)
class BlockAdmin(admin.ModelAdmin):
    list_display = [
        "id", "from_user","to_user"
    ]


