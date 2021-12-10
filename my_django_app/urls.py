# Here  I create my templates by writing the urls adresses
from django.contrib import admin
from django.urls import path, include
from women.views import categories, pageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('women.urls')),

]
handler404 = pageNotFound
