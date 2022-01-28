from django.urls import path, include
from .views import get_characters, get_charater_quotes, add_favorite
urlpatterns = [
    path('', get_characters, name='get_character' ),
    path('<str:pk>/quotes/', get_charater_quotes, name='get_charater_quotes'),
    path('<str:pk>/favorites/', add_favorite, name='add_favorite')
]
