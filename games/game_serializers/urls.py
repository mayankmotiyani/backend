from django.urls import path
from .views import (
    GameAPI,
    GameContentAPI
)


urlpatterns = [

    path('game_list/',GameAPI.as_view(),name='game-list'),
    path('<slug:game_slug>/',GameContentAPI.as_view(),name='game')
]