from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import BlogPost

User = get_user_model()


class AuthorBlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class BlogPostListSerializer(serializers.ModelSerializer):
    author = AuthorBlogPostSerializer(read_only=True)

    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'content', 'author')
        read_only_fields = ('id',)
