from django.contrib import admin

from books.models import BookModel


@admin.register(BookModel)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'name', 'description', 'author', 'price', 'category', 'created_at', 'updated_at')
    list_display_links = ('id', 'image', 'name', 'description', 'author', 'price', 'category', 'created_at',
                          'updated_at')
    list_filter = ('category', 'created_at', 'updated_at')
    search_fields = ('name', 'description', 'author', 'price', 'category')
    list_per_page = 20
    readonly_fields = ('created_at', 'updated_at')
