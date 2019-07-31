from django import forms
from .models import *

class TopicForm(forms.ModelForm):
    '''创建一个分享观点或问题的表单'''
    class Meta:
        model = Topic
        fields = ['topic']
        #不要为topic生成标签？
        labels = {'topic': ''}
        widgets = {'topic': forms.Textarea(attrs={'cols': 80,'rows': '10'})}