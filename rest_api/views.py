from rest_framework import generics
from .models import Article
from .serializers import ArticlesSerializer


# Handles the '/api/articles' request and returns the response (paginated list of articles)
class ListArticlesView(generics.ListAPIView):
    model = Article
    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer
