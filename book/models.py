from django.db import models

# Create your models here.

class Book(models.Model):
    '''python书目'''
    name = models.CharField(max_length=30)

    def __str__(self):
        '''返回字符串'''
        return self.name

class Chapter(models.Model):
    '''章'''
    name = models.CharField(max_length=30)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        '''返回'''
        return self.name

class Topic(models.Model):
    '''分享的观点或者问题'''
    topic = models.CharField(max_length=50)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)

    def __str__(self):
        '''返回'''
        return self.topic


class Entry(models.Model):
    '''关于某个主题的讨论'''
    entry = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        '''返回前50个字'''
        return self.entry[:50] + '...'
