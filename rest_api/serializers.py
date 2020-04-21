from rest_framework import serializers
from .models import Article

# Serializer for the Article Model.
class ArticlesSerializer(serializers.ModelSerializer):

    # This ensures that the Authors first_name and last_name are serialized to the author field and not the author.id
    author = serializers.CharField(source='author.__str__', read_only=True)

    class Meta:
        model = Article
        fields = ("title", "summary","content", "published_status","published_date", "category", "author")