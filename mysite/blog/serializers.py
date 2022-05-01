from rest_framework import serializers
from .models import Post, UserFollowing

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content')

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserFollowing
        fields = ('user_id')
