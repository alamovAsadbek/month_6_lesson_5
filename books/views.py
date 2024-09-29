from django.shortcuts import render

from books.models import BookModel


def booksView(request):
    all_books = BookModel.objects.all()
    context = {'books': all_books}
    return render(request, 'index.html', context)


def bookDetailView(request, book_id):
    return render(request, 'card.html', {'book_id': book_id})


def createBookView(request):
    return render(request, 'add-book.htmll')
