from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(Topic)
admin.site.register(Entry)