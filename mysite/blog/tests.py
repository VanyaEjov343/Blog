from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post


class BlogTest(TestCase):

    def setUp(self):
        self.user = get_user_model().object.create_user(
            username='testuser',
            email='test@email.com',
            password= 'secret'
        )
        self.post = Post.objects.create(
            title='A nice title',
            body='nice content',
            author=self.user,
        )

# Create your tests here.
