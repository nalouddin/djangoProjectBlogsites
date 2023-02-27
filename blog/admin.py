from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Person)
admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Reaction)
admin.site.register(Comment)