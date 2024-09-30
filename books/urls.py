from django.urls import path

from books.views import booksView, bookDetailView, createBookView

urlpatterns = [
    path('', booksView),
    path('<int:book_id>/', bookDetailView, name='book_detail'),
    path('add/', createBookView, name='create_book'),
]
