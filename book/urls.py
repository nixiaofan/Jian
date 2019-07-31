from django.conf.urls import url
from . import views as v

urlpatterns = [
    #首页
    url(r'^$', v.index, name='index'),
    #显示所有书目
    url(r'^books/$', v.books, name='books'),
    #显示特定书目
    url(r'^books/(?P<book_id>\d+)/$', v.book, name='book'),
    #显示特定的章节以及里面的部分答复
    url(r'^books/(?P<book_id>\d+)/$', v.book, name='book'),
]