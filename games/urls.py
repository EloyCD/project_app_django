from django.urls import path
from .views import gamesView

urlpatterns = [
    path('', gamesView, name="games")
]