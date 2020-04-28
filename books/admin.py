from django.contrib import admin
from .models import Books, Comments

class CommentAdmin(admin.ModelAdmin):
    list_display = ('books', 'comment_title', 'comment', 'pub_date', 'active')
    list_filter = ('active', 'pub_date', 'updated')
    search_fields = ('comment_title', 'author', 'comment')


admin.site.register(Books)
admin.site.register(Comments, CommentAdmin)