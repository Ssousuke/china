from unicodedata import category
from django.test import TestCase
from apps.blog.models import Category, Post, User


class BlogTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    @staticmethod
    def create_user():
        return User.objects.create_user(
            first_name='user',
            last_name='name',
            username='username',
            password='123456',
            email='username@gmail.com',
        )

    @staticmethod
    def make_category():
        return Category.objects.create(
            name='What is Lorem Ipsum?'
        )
    
    def make_post(self):
        return Post.objects.create(
            title='Why do we use it?',
            body='Lorem Ipsum is simply dummy text of the printing and typesetting industry.',
            category=self.make_category(),
            author=self.create_user(),
            published=True,
        )
