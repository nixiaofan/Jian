from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
#从核心-解析器导入反向解析
from django.core.urlresolvers import reverse
from .forms import TopicForm

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

def new_topic(request, chapter_id):
    '''在指定章节下面生成新的话题'''
    #指定章节
    chapter = Chapter.objects.get(id=chapter_id)

    if request.method != 'POST':
        #没有提交数据，创建一个新的表单
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            #新问题保存在new_topic中，而不保存在数据库中
            new_topic = form.save(commit=False)
            #指定多对一属性
            new_topic.chapter = chapter
            #然后再保存
            new_topic.save()

            #重定向到章节的所有的问题页面
            return HttpResponseRedirect(reverse('book:chapter', args=[chapter_id]))

    context = {'form': form, 'chapter': chapter}
    return render(request, 'book/new_topic.html', context)