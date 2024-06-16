from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path('', views.home, name='home'),
    path('articles/', views.article_list, name='article_list'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('i18n/', include('django.conf.urls.i18n')),
)
