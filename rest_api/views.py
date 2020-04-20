from django.shortcuts import render
from rest_framework import generics
from .models import Article
from .serializers import ArticlesSerializer

# Create your views here.

# Handles the /articles request and returns the response (list of articles)
class ListArticlesView(generics.ListAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer