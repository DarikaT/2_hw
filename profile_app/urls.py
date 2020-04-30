from django.urls import path
from .views import *

urlpatterns = [
    path('signup-book/', UserSignUpView.as_view(), name = 'signup_url'),
    path('profile/edit/', edit, name='profile_edit_url'),
    path('profile/<int:pk>/',profile_detail, name = 'profile_url'),
]   