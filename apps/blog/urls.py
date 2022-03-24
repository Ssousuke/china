from django.urls import path
from .import views


app_name = 'blog'
urlpatterns = [
    # post
    path('', views.home, name='home'),
    path('<slug:slug>/', views.detail, name='detail'),

    # category
    path('categorias/a/', views.categories, name='categories'),
    path('categorias/a/<slug:slug>/', views.category, name='category'),
]
