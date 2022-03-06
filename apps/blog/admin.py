from django.contrib import admin
from . models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'category',
        'author',
        'created_at',
        'updated_at',
        'published'
    ]

    list_display_links = [
        'title',
        'category',
        'author',
        'created_at',
        'updated_at'
    ]

    list_editable = [
        'published'
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'created_at',
        'updated_at',
    ]

    list_display_links = [
        'name',
        'created_at',
        'updated_at',
    ]
