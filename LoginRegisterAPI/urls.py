from django.urls import path 
from .views import registerView,loginView,VerifyEmail



urlpatterns = [
    path('register',registerView.as_view()),
    path('login',loginView.as_view()),
    path('email-verify/', VerifyEmail.as_view(), name = 'email-verify')
]