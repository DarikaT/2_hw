from django.views.generic import ListView, DetailView
from .models import Books, Comments
from django import forms
from django.shortcuts import render
from django.views.generic.edit import (
    CreateView, 
    UpdateView,
    DeleteView,
    )
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



class BooksListView(ListView):
    model = Books
    template_name = 'books_list.html'
    paginate_by = 3



class BooksDetailView(DetailView):
    model = Books
    template_name = 'book_detail.html'


class BooksNew(ListView):
    model = Books
    template_name = 'books_new.html'
    paginate_by = 3


class WhatToRead(ListView):
    model = Books
    template_name = 'books_random.html'
    paginate_by = 3


class BooksCreateView(CreateView):
    model = Books
    template_name = 'books_create.html'
    fields = ('title', 'author', 'image', 'book')
    initial = {"title": "Название книги", 'book': 'Напишите свою аннотацию'}


class BooksUpdateView(UpdateView):
    model = Books
    template_name = 'books_update.html'
    fields = ('title', 'image', 'book')
    

class BookDeleteView(DeleteView):
    model = Books
    template_name = 'books_delete.html'
    success_url = reverse_lazy('bookslist_url')