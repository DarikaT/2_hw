from django.db import models
from django.urls import reverse
from django.utils import timezone

class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media', blank=True)
    book = models.TextField()
    publish = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('bookdetail_url', args=[str(self.id)])

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

class Comments(models.Model):
    comment = models.TextField()
    books = models.ForeignKey(Books, on_delete=models.CASCADE, related_name= 'book_comments')
    pub_date = models.DateTimeField('Дата комментария', default=timezone.now)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

        



