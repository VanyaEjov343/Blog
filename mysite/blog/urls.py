from django.urls import path
from .views import BlogListView, PostDetailsView


urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('', PostDetailsView.as_view()),
]
