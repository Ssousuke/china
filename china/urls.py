from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/admin/china/', admin.site.urls),
    path('', include('apps.blog.urls', namespace='blog')),
    path('cms/', include('apps.cms.urls', namespace='cms')),
    path('about/', include('apps.about.urls', namespace='about')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)


handler404 = 'apps.blog.views.error_404'