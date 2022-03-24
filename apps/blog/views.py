from django.shortcuts import render, get_object_or_404
from apps.blog.models import Post, Category


def home(request):
    template_name = 'blog/home.html'
    list_categories = Category.objects.all()
    list = Post.objects.filter(published=True)
    return render(request, template_name, {'list': list, 'categories': list_categories})


def detail(request, slug):
    template_name = 'blog/detail.html'
    list_categories = Category.objects.all()
    detail = get_object_or_404(Post, published=True, slug=slug)
    return render(request, template_name, {'detail': detail, 'categories': list_categories})


def categories(request):
    template_name = 'blog/categories.html'
    list = Category.objects.all()
    return render(request, template_name, {'list': list})


def category(request, slug):
    template_name = 'blog/home.html'
    category = Category.objects.get(slug=slug)
    list = Post.objects.filter(category=category, published=True)
    return render(request, template_name, {'list': list})
