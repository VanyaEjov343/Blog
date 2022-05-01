from django.urls import path, include
from .views import BlogListView, PostDetailsView, PostViewSet
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Posts', views.PostViewSet)

urlpatterns = [
    path('post/<int:pk>/', PostDetailsView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
]
