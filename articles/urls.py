from django.urls import path
from .views import (ArticleListView, ArticleDeleteView, ArticleUpdateView, ArticleDetailView, ArticleCreateView)

urlpatterns = [
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='articles_delete'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='articles_edit'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='articles_detail'),
    path('new/', ArticleCreateView.as_view(), name='articles_new'),
    path('', ArticleListView.as_view(), name='articles_list'),
]