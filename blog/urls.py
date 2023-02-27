from django.urls import path
from .views import *

urlpatterns = [
    path('', articles, name = 'articles'),
    path('article/<int:id>', article_detail, name = 'article_detail'),
]