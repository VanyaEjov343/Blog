from django.urls import path
from .views import BlogListView, PostDetailsView, PostViewSet
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Posts', views.PostViewSet)

urlpatterns = [
    path('post/<int:pk>/', PostDetailsView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
    path('', PostViewSet.as_view(), name='api'),

]
