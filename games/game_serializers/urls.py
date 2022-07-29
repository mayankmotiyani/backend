from django.urls import path
from .views import (
    GameAPI
)


urlpatterns = [

    path('game_list/',GameAPI.as_view(),name='game-list')
]