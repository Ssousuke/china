from django.shortcuts import render
from django.views import generic
from apps.about.models import Job


class AboutListView(generic.ListView):
    template_name = 'about/about.html'
    model = Job
    context_object_name = 'jobs'
