from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post

from django.views.generic import ListView, DetailView


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailsView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostSerializer

