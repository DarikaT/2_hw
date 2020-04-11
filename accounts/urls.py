from django.urls import path
from .views import BooksSignUpView

urlpatterns = [
    path('signup/', BooksSignUpView.as_view(), name = 'signup_url'),
]