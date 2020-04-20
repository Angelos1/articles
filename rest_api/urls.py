from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.ListArticlesView.as_view(), name='articles'),


]
