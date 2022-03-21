from django.urls import path
from . import views

app_name = 'cms'
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('pages/posts/', views.posts, name='posts'),
    path('pages/posts/published/filter/<str:post_filter>/', views.posts, name='post'),
    path('pages/posts/edit/<slug:slug>/', views.PostUpdateForm.as_view(), name='edit_post'),
    path('pages/posts/new/', views.PostCreateForm.as_view(), name='new_post'),
]
