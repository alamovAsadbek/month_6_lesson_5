from django.urls import path

from books.views import booksView

urlpatterns = [
    path('', booksView),
    path('<int:book_id>/', bookView)
]
