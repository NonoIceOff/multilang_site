from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from main import views

## BASIC REDIRECTIONS ##
urlpatterns = [
    path('admin/', admin.site.urls),
]

## REDIRECTIONS WITH TRANSLATIONS ##
urlpatterns += i18n_patterns(
    path('', views.home, name='home'), ## REDIRECT THE DEFINITION home FROM views TO THE PAGE ##
    path('articles/', views.article_list, name='article_list'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('search/', views.search, name='search'),
    path('result/', views.search_results, name='search_results'),
    path('i18n/', include('django.conf.urls.i18n')),
)
