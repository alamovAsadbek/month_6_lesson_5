from django.urls import path

from books.views import booksView, bookDetailView

urlpatterns = [
    path('', booksView),
    path('<int:book_id>/', bookDetailView)
]
