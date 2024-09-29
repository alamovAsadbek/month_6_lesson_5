from django.urls import path

from books.views import booksView, bookDetailView, createBookView

urlpatterns = [
    path('', booksView),
    path('<int:book_id>/', bookDetailView),
    path('add/', createBookView),
]
