from django.contrib import admin
from apps.about.models import TypeJob, Job


@admin.register(TypeJob)
class TypeJobAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'type',
        'created_at',
        'updated_at'
    ]
    list_display_links = [
        'id',
        'type',
        'created_at',
        'updated_at'
    ]


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'job',
        'initial_date',
        'finish_date',
        'type',
        'link',
        'created_at',
        'updated_at',
        'status',
    ]
    list_display_links = [
        'id',
        'job',
        'initial_date',
        'finish_date',
        'type',
        'link',
        'created_at',
        'updated_at',
    ]
    list_editable = [
        'status',
    ]
