from rest_framework import serializers
from .models import Product, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'product', 'description']


class ProductSerializer(serializers.ModelSerializer):
    # Include related comments (optional)
    comments = CommentSerializer(many=True, read_only=True, source='comment_set')
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'created_at', 'updated_at', 'comments']
        read_only_fields = ['created_at', 'updated_at']
