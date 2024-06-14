from django.shortcuts import render
from .models import Article

def home(request):
    return render(request, 'main/home.html')


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'main/article_list.html', {'articles': articles})