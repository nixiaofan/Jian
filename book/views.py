from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    return render(request, 'book/index.html')

def books(request):
    '''显示所有书目'''
    books = Book.objects.order_by('id')
    context = {'books': books}
    return render(request, 'book/books.html', context)

def book(request, book_id):
    book = Book.objects.get(id=book_id)
    chapters = book.chapter_set.order_by('id')
    context = {'book': book, 'chapters': chapters}
    return render(request, 'book/book.html', context)