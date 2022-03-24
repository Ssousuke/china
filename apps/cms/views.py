from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from apps.blog.models import Post, Category
from apps.cms.forms import PostForm, CategoryForm


@login_required
def dashboard(request):
    template_name = 'cms/dashboard.html'
    active_posts = Post.objects.filter(published=True).count
    inactive_posts = Post.objects.filter(published=False).count
    categories = Category.objects.all().count
    context = {
        'active_posts': active_posts,
        'inactive_posts': inactive_posts,
        'categories': categories,
    }
    return render(request, template_name, context)


@login_required
def posts(request):
    template_name = 'cms/list_posts.html'
    posts = Post.objects.all()
    return render(request, template_name, {'posts': posts})


class PostUpdateForm(LoginRequiredMixin, UpdateView):
    template_name = 'cms/post_form.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('cms:posts')

    def form_valid(self, form):
        form.save()
        return super(PostUpdateForm, self).form_valid(form)


class PostCreateForm(LoginRequiredMixin, CreateView):
    template_name = 'cms/post_form.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('cms:posts')

    def form_valid(self, form):
        form.save()
        return super(PostCreateForm, self).form_valid(form)


@login_required
def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('cms:posts')


@login_required
def categories(request):
    template_name = 'cms/list_category.html'
    categories_list = Category.objects.all()
    return render(request, template_name, {'categories': categories_list})


@login_required
def create_category(request):
    template_name = 'cms/category_form.html'
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('cms:categories')
    return render(request, template_name, {'form': form})


@login_required
def delete_category(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return redirect('cms:categories')


class UpdateCategory(LoginRequiredMixin, UpdateView):
    template_name = 'cms/category_form.html'
    form_class = CategoryForm
    model = Category
    success_url = reverse_lazy('cms:categories')
