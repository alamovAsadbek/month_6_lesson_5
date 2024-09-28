from django.urls import path

from books.views import booksView

urlpatterns = [
    path('', booksView, name='book_list'),
]
