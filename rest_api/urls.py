from django.urls import path
from . import views

# directs the request of '/api/articles' to be processed by the ListArticlesView
urlpatterns = [
    path('articles/', views.ListArticlesView.as_view(), name='articles'),

]
