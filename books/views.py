from django.shortcuts import render, redirect

from books.forms import BookModeForm
from books.models import BookModel


def booksView(request):
    all_books = BookModel.objects.all()
    context = {'books': all_books}
    return render(request, 'index.html', context)


def bookDetailView(request, book_id):
    return render(request, 'card.html', {'book_id': book_id})


def createBookView(request, *args, **kwargs):
    if request.method == 'POST':
        form = BookModeForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save()
            return redirect('/')
    return render(request, 'add-book.html')
