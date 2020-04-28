from django.urls import path
from .views import (
    BooksListView, 
    BooksDetailView, 
    BooksNew, 
    WhatToRead, 
    BooksCreateView, 
    BooksUpdateView, 
    BookDeleteView,
)
from .models import Books

urlpatterns = [
    # path('books/<int:pk>/deletecomment/', CommentsDeleteView.as_view(), name = 'commentsdelete_url'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name = 'bookdelete_url'),
    path('books/<int:pk>/edit/', BooksUpdateView.as_view(), name = 'bookupdate_url'),
    path('books/create/', BooksCreateView.as_view(), name = 'bookcreate_url'),
    path('whattoread/', WhatToRead.as_view(queryset = Books.objects.all().order_by('?')), name = 'whattoread_url'),
    path('newbooks/', BooksNew.as_view(queryset = Books.objects.all().order_by('-publish')), name = 'booksnew_url'),
    path('books/<int:pk>/', BooksDetailView.as_view(), name = 'bookdetail_url'),
    path('', BooksListView.as_view(), name = 'bookslist_url'),
    
]