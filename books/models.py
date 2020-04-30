from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core import validators
from django.core.exceptions import ValidationError
from django.conf import settings


class Books(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField('Название книги', max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='book_posts')
    image = models.ImageField('Изображение:', upload_to='media', blank=True)
    book = models.TextField('Аннотация', validators=[validators.MinLengthValidator(400,message='Минимальное количество символов: 400')])
    publish = models.DateTimeField('Дата публикации', default=timezone.now)
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Дата обновления', auto_now=True)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    status = models.CharField('Статус', max_length=10, choices=STATUS_CHOICES, default='draft')
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='books_liked', blank=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-publish',)
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

class Comments(models.Model):
    comment_title = models.CharField('Заголовок',max_length=80)
    comment = models.TextField('Комментарий')
    books = models.ForeignKey(Books, on_delete=models.CASCADE, related_name= 'book_comments')
    pub_date = models.DateTimeField('Дата комментария', default=timezone.now)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE
    )
    updated = models.DateTimeField('Обновлено', auto_now=True)
    active = models.BooleanField('Активные',default=True)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('bookdetail_url')

    class Meta:
        ordering =('-pub_date', )
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return 'Comment by {} on {}'.format(self.comment_title, self.books)

        



