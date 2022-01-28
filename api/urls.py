from django.urls import path, include
from .views import list
urlpatterns = [
    path('', list, name='list' )
]
