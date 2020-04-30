from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm, EmailBooksForm
from django.views.generic import ListView, DetailView
from django.core.exceptions import PermissionDenied
from .models import Books, Comments
from profile_app.models import Profile
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
# from django.core.mail import send_mail

class BooksListView(GetQuerySetMixin, ListView):
    model = Books
    template_name = 'books_list.html'
    paginate_by = 5
    
        

class BooksDetailView(FormView, DetailView):
    model = Books
    form_class = CommentForm
    template_name = 'book_detail.html'
    # comments = Books.book_comments.filter(active=True)

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('bookdetail_url', kwargs={'pk': self.get_object().pk})

    def form_valid(self, form):
        form = form.save(commit=False)
        form.books = self.get_object()
        form.author = self.request.user
        form.save()
        return super().form_valid(form)             #разобраться

    #не работает. почему - не знаю. должен убирать неактивные комментарии с сайта.
    def book_detail(request, year, month, day, books):
        book = get_object_or_404(Books, status='published', publish__year=year, publish__month=month, publish__day=day )

        comments = book.book_comments.filter(active=True)
        
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
    success_url = reverse_lazy('bookslist_url')

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

# def book_share(request, book_id):
#     # Retrieve post by id
#     book_post = get_object_or_404(Books, id=books_id, status='published')
#     sent = False
#     if request.method == 'POST':
#         # Form was submitted
#         form = EmailBooksForm(request.POST)
#         if form.is_valid():
#             # Form fields passed validation
#             cd = form.cleaned_data
#             book_post_url = request.build_absolute_uri(book_post.get_absolute_url())
#             subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], book_post.title)
#             message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(book_post.title, book_post_url, cd['name'], cd['comments'])
#             send_mail(subject, message, 'admin@myblog.com',[cd['to']])
#             sent = True
#     else:
#         form = EmailBooksForm()
#     return render(request, 'other/share.html', {'book_post': book_post,
#                                                     'form': form,
#                                                     'sent': sent})