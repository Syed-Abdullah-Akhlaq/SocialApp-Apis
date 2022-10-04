from django.urls import path,include
from .views import CRUDviews,getOwner,CRUDDetails,PostModelViewSet
# ,CRUDDetails
from django.urls import re_path as url
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'PostModelViewSet', PostModelViewSet, basename= 'PostModelViewSet')




urlpatterns = [
    path('',CRUDviews.as_view()),
    path('a/<int:owner>/',getOwner),
    path('<int:id>',CRUDDetails.as_view()),
    url(r'api/', include(router.urls)),
]