from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/games/', include('games.urls')),  # Incluye las URLs de la aplicación games API
]


