from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from apps.utils.base_models import Base
from django_extensions.db.fields import AutoSlugField


def slugify_function(content):
    return content.replace('_', '-').lower()


class Category(Base):
    name = models.CharField(max_length=80)
    thumb = models.ImageField(upload_to='category/thumb', blank=True)
    slug = AutoSlugField(populate_from='name', unique=True, editable=False)

    def __str__(self) -> str:
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']


class Post(Base):
    thumb = models.ImageField(upload_to='category/thumb', blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    body = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from='title', unique=True, editable=False)
    views = models.IntegerField(editable=False, default=0)

    def __str__(self) -> str:
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'
        ordering = ['-updated_at']
