from django.urls import path ,include
from .views import send_friend_request,accept_friend_request,ignore_friend_request,revert_friend_request,block_friend_request
from rest_framework.routers import DefaultRouter
from .views import UserModelViewSet
from django.urls import re_path as url
from rest_framework import routers
from .views import ChangePasswordView

router = routers.DefaultRouter()
router.register(r'users', UserModelViewSet, basename='users')

urlpatterns = [
    path('send_friend_request/<int:UserID>',send_friend_request),
    path('accept_friend_request/<int:requestID>',accept_friend_request),
    path('ignore_friend_request/<int:requestID>',ignore_friend_request),
    path('revert_friend_request/<int:requestID>',revert_friend_request),
    path('block_friend_request/<int:userID>',block_friend_request),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    url(r'^api/', include(router.urls)),
]