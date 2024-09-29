from django.shortcuts import render, redirect

from books.forms import BookModelForm
from books.models import BookModel
from categories.models import CategoryModel


def booksView(request):
    all_books = BookModel.objects.all()
    # categories = BookModel.objects.values_list('category', flat=True).distinct()
    context = {'books': all_books}
    return render(request, 'index.html', context)


def bookDetailView(request, book_id):
    return render(request, 'card.html', {'book_id': book_id})


def createBookView(request, *args, **kwargs):
    categories = CategoryModel.objects.all()
    context = {'categories': categories}
    if request.method == 'POST':
        form = BookModelForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save()
    return redirect('/')
