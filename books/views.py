from django.shortcuts import render


def booksView(request):
    return render(request, 'index.html')


def bookDetailView(request, book_id):
    return render(request, 'card.html', {'book_id': book_id})
