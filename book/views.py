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
    '''书的章节'''
    book = Book.objects.get(id=book_id)
    chapters = book.chapter_set.order_by('id')
    context = {'book': book, 'chapters': chapters}
    return render(request, 'book/book.html', context)

def chapter(request, chapter_id):
    '''章节里面内容'''
    chapter = Chapter.objects.get(id=chapter_id)
    book = chapter.book
    topics = chapter.topic_set.order_by('id')
    context = {'chapter': chapter, 'topics':topics, 'book': book}
    return render(request, 'book/chapter.html', context)

def topic(request, topic_id):
    '''讨论话题的全部内容'''
    topic = Topic.objects.get(id=topic_id)
    chapter = topic.chapter
    entries = topic.entry_set.order_by('id')
    context = {'topic': topic, 'entries': entries, 'chapter': chapter}
    return render(request, 'book/topic.html', context)