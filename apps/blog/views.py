from django.shortcuts import render, get_object_or_404
from apps.blog.models import Post, Category


def home(request):
    template_name = 'blog/home.html'
    list = Post.objects.filter(published=True)
    return render(request, template_name, {'list': list})


def detail(request, slug):
    template_name = 'blog/detail.html'
    detail = get_object_or_404(Post, slug=slug)
    return render(request, template_name, {'detail': detail})


def categories(request):
    template_name = 'blog/categories.html'
    list = Category.objects.all()
    return render(request, template_name, {'list': list})


def category(request, slug):
    template_name = 'blog/home.html'
    category = Category.objects.get(slug=slug)
    list = Post.objects.filter(category=category)
    return render(request, template_name, {'list': list})
