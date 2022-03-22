from django.forms import ModelForm
from django import forms
from apps.blog.models import Post, Category


class SearchPost(ModelForm):
    class Meta:
        model = Post
        fields = ['published']


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['thumb']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '3'
                }
            ),
            'body': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '20'
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'published': forms.CheckboxInput(
                attrs={
                    'class': 'checkbox',
                }
            ),
        }


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        exclude = ['thumb']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }
