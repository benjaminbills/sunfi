from django.urls import path, include
from .views import add_favorite_quote, get_characters, get_charater_quotes, add_favorite
urlpatterns = [
    path('', get_characters, name='get_character' ),
    path('<str:pk>/quotes/', get_charater_quotes, name='get_charater_quotes'),
    path('<str:pk>/favorites/', add_favorite, name='add_favorite'),
    path('<str:pk_c>/quotes/<str:pk_q>/favorites/', add_favorite_quote, name='add_favorite_quote')
]
