# Here  I create my templates by writing the urls adresses
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from my_django_app import settings
from women.views import categories, pageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('women.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound
