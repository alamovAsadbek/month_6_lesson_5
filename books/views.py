from django.shortcuts import render


def booksView(request):
    return render(request, 'index.html')
