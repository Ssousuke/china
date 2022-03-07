from apps.blog.tests.test_base import BlogTestBase
from django.urls import reverse


class TestBlogView(BlogTestBase):
    def test_home(self):
        home = self.client.get(reverse('blog:home'))
        self.assertTemplateUsed(home, 'blog/home.html')
        self.assertEqual(home.status_code, 200)

    def test_detail(self):
        post_detail = self.make_post()
        post_detail.save()
        detail = self.client.get(
            reverse('blog:detail', kwargs={'slug': post_detail.slug}))
        self.assertTemplateUsed(detail, 'blog/detail.html')
        self.assertEqual(detail.status_code, 200)
        self.assertEqual(post_detail.get_absolute_url(),
                         f'/{post_detail.slug}/')

    def test_categories(self):
        categories = self.client.get(reverse('blog:categories'))
        self.assertTemplateUsed(categories, 'blog/categories.html')
        self.assertEqual(categories.status_code, 200)

    def test_category(self):
        cat = self.make_category()
        cat.save()
        category = self.client.get(
            reverse('blog:category', kwargs={'slug': cat.slug}))
        self.assertTemplateUsed(category, 'blog/home.html')
        self.assertEqual(category.status_code, 200)
        self.assertEqual(cat.get_absolute_url(), f'/categorias/{cat.slug}/')
