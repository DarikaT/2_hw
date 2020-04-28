from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from django.core import validators
from django.core.exceptions import ValidationError


class Books(models.Model):
    title = models.CharField('Название книги', max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ImageField('Изображение:', upload_to='media', blank=True)
    book = models.TextField('Аннотация', validators=[validators.MinLengthValidator(400,message='Минимальное количество символов: 400')])
    publish = models.DateTimeField('Дата публикации', default=timezone.now)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('bookdetail_url', args=[str(self.id)])

    class Meta:
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

        



