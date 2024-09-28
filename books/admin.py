from django.contrib import admin

from books.models import BookModel


@admin.register(BookModel)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'name', 'description', 'author', 'price', 'category', 'created_at', 'updated_at')
