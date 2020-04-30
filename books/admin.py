from django.contrib import admin
from .models import Books, Comments

class CommentAdmin(admin.ModelAdmin):
    list_display = ('books', 'comment_title', 'comment', 'pub_date', 'active')
    list_filter = ('active', 'pub_date', 'updated')
    search_fields = ('comment_title', 'author', 'comment')


class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

admin.site.register(Books, BooksAdmin)
admin.site.register(Comments, CommentAdmin)