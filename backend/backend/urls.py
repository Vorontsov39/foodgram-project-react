from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api/', include('users.urls')),
    path('api/', include('foodgram.urls')),
    path('admin/', admin.site.urls),
]
