from apps.blog.models import slugify_function
from apps.blog.tests.test_base import BlogTestBase


class TestBlogModels(BlogTestBase):
    def test_return__str__category(self):
        category = self.make_category()
        category.save()
        self.assertEqual(category.__str__(), category.name)

    def test_return__str__post(self):
        post = self.make_post()
        post.save()
        self.assertEqual(post.__str__(), post.title)

    def test_slugfy_function(self):
        slug = slugify_function('Olá-Mundo!')
        self.assertEqual(slug, 'olá-mundo!')
