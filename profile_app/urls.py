from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', BooksSignUpView.as_view(), name = 'signup_url'),
    path('profile/edit/', edit, name='profile_edit_url'),
    path('profile/<int:pk>', ProfileView.as_view(), name = 'profile_url'),
    path('profile/create/', CreateProfile.as_view(), name = 'profilecreate_url'),
]