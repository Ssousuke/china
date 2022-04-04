from django.urls import path
from . import views

app_name = 'about'
urlpatterns = [
    path('jobs/', views.AboutListView.as_view(), name='about'),
]
