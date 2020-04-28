from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm
from django.views.generic import ListView, DetailView
from django.core.exceptions import PermissionDenied
from .models import Books, Comments
from django import forms
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import (
    CreateView, 
    UpdateView,
    DeleteView,
    FormView,
    )
from django.urls import reverse_lazy
from .mixins import DispatchFuncMixin, GetQuerySetMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




class BooksListView(GetQuerySetMixin, ListView):
    model = Books
    template_name = 'books_list.html'
    paginate_by = 5

class BooksDetailView(FormView, DetailView):
    model = Books
    form_class = CommentForm
    template_name = 'book_detail.html'

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('bookdetail_url', kwargs={'pk': self.get_object().pk})

    def form_valid(self, form):
        form = form.save(commit=False)
        form.books = self.get_object()
        form.author = self.request.user
        form.save()
        return super().form_valid(form)             #разобраться


    def book_detail(request, year, month, day, books):
        book = get_object_or_404(Books, publish__year=year, publish__month=month, publish__day=day )

        comments = post.book_comments.filter(active=True)
        
class BooksNew(ListView):
    model = Books
    template_name = 'books_new.html'
    paginate_by = 3


class WhatToRead(ListView):
    model = Books
    template_name = 'books_random.html'
    paginate_by = 4


class BooksCreateView(LoginRequiredMixin, CreateView):
    model = Books
    template_name = 'books_create.html'
    fields = ('title', 'image', 'book')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user #instance - экземпляр класса books; request и user встроены в createview
        return super().form_valid(form)

class BooksUpdateView(LoginRequiredMixin, DispatchFuncMixin, UpdateView):
    model = Books
    template_name = 'books_update.html'
    fields = ('title', 'image', 'book')
    login_url = 'login'

class BookDeleteView(LoginRequiredMixin, DispatchFuncMixin, DeleteView):
    model = Books
    template_name = 'books_delete.html'
    success_url = reverse_lazy('bookslist_url')
    login_url = 'login'

# class CommentsDeleteView(DeleteView):
#     model = Comments
#     template_name = 'book_detail.html'
#     success_url = reverse_lazy('bookdetail_url')

