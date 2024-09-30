from django.shortcuts import render, redirect, get_object_or_404

from books.forms import BookModelForm
from books.models import BookModel
from categories.models import CategoryModel


def booksView(request):
    all_books = BookModel.objects.all()
    context = {'books': all_books}
    return render(request, 'index.html', context)


def bookDetailView(request, book_id):
    book = BookModel.objects.get(id=book_id)
    context = {'book': book}
    return render(request, 'card.html', context)


def createBookView(request, *args, **kwargs):
    categories = CategoryModel.objects.all()
    context = {'categories': categories}
    if request.method == 'POST':
        form = BookModelForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save()
            return redirect('/')
    return render(request, 'add-book.html', context)


def updateBookView(request, book_id):
    book = get_object_or_404(BookModel, id=book_id)
    categories = CategoryModel.objects.all()
    context = {'book': book, 'categories': categories}
    if request.method == 'POST':
        form = BookModelForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'edit-book.html', context)
