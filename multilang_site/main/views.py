from django.shortcuts import render, get_object_or_404
from .models import Article
from django.utils.translation import gettext as _

def home(request):
    return render(request, 'main/home.html')

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'main/article_list.html', {'articles': articles})
    
def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'main/article_detail.html', {'article': article})
