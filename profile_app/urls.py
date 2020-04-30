from django.urls import path
from .views import *

urlpatterns = [
    path('signup-book/', UserSignUpView.as_view(), name = 'signup_url'),
    path('profile/edit/', edit, name='profile_edit_url'),
    path('profile/<int:pk>/', ProfileView.as_view(), name = 'profile_url'),
]   