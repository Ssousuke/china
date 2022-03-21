from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView

from apps.blog.models import Post
from apps.cms.forms import PostForm


@login_required
def dashboard(request):
    template_name = 'cms/dashboard.html'
    return render(request, template_name)


@login_required
def posts(request):
    template_name = 'cms/list_posts.html'
    if request.method == 'POST':
        post_filter = request.POST.get('filter')
        posts = Post.objects.filter(published=post_filter)
        if not post_filter:
            posts = Post.objects.all()
        return render(request, template_name, {'posts': posts})
    return render(request, template_name)


class PostUpdateForm(LoginRequiredMixin, UpdateView):
    template_name = 'cms/post_form.html'
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.save()
        return super(PostUpdateForm, self).form_valid(form)


class PostCreateForm(LoginRequiredMixin, CreateView):
    template_name = 'cms/post_form.html'
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.save()
        return super(PostCreateForm, self).form_valid(form)
