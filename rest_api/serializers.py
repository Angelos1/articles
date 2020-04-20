from rest_framework import serializers
from .models import Article

# Serializer for the Article Model. Serializes the data to Python types and the reverse
class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title", "summary","content", "published_status","published_date", "category","author")