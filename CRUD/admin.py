from django.contrib import admin

from CRUD.models import CRUD,Post,LikePost,CommentPost

# Register your models here.
@admin.register(CRUD)
class AdminCRUD(admin.ModelAdmin):
    list_display = ['owner','id','country_code', 'first_name', 'last_name', 'phone_number', 'contact_picture', 'is_favorite']




@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'post']



@admin.register(LikePost)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'userLike']



@admin.register(CommentPost)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'userComment']