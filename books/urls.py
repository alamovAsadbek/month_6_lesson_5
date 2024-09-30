from django.urls import path

from books.views import booksView, bookDetailView, createBookView, updateBookView, deleteBookView

urlpatterns = [
    path('', booksView),
    path('<int:book_id>/', bookDetailView, name='book_detail'),
    path('add/', createBookView, name='create_book'),
    path('edit/<int:book_id>/', updateBookView, name='edit_book'),
    path('delete/<int:book_id>/', deleteBookView, name='delete_book'),
]
