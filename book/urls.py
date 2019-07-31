from django.conf.urls import url
from . import views as v

urlpatterns = [
    #首页
    url(r'^$', v.index, name='index'),
    #显示所有书目
    url(r'^books/$', v.books, name='books'),
    #显示特定书目
    url(r'^books/(?P<book_id>\d+)/$', v.book, name='book'),
    #显示特定的章节里面的讨论话题
    url(r'^chapter/(?P<chapter_id>\d+)/$', v.chapter, name='chapter'),
    #显示讨论话题的全部讨论内容
    url(r'^topic/(?P<topic_id>\d+)/$', v.topic, name='topic'),
    #添加新的讨论话题
    url(r'^new_topic/(?P<chapter_id>\d+)/$', v.new_topic, name='new_topic'),

]