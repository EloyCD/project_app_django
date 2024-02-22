from django.urls import path
from .views import GameListCreateAPIView, GameDetailAPIView

app_name = 'games'  # Namespace de la aplicación

urlpatterns = [
    path('', GameListCreateAPIView.as_view(), name='game_list_api'),  # Ruta para la lista de juegos API
    path('<int:pk>/', GameDetailAPIView.as_view(), name='game_detail_api'),  # Ruta para los detalles de un juego específico API
]


