
# Here  I create my templates by writing the urls adresses
from django.contrib import admin
from django.urls import path, include
from women.views import categories



urlpatterns = [
    path('admin/', admin.site.urls),
    path('women/', include('women.urls')),

]
