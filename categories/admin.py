from django.contrib import admin

from categories.models import CategoryModel


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    list_display_links = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
