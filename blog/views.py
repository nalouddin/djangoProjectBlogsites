from django.shortcuts import render
from .models import *

# Create your views here.

def articles(request):
    articles = Article.objects.all().order_by('created_date')
    return render(
        request=request,
        template_name='index.html',
         context={
             'articles': articles
         }
    )

def article_detail(request, id):
    article = Article.objects.get(id=id)
    likes = article.reactions.filter(reaction='like').count()
    dislikes = article.reactions.filter(reaction='dislike').count()
    return render(
        request=request,
        template_name='article_detail.html',
         context={
             'article': article,
             'likes': likes,
             'dislikes': dislikes
         }
    )