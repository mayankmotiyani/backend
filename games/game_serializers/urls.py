from django.urls import path
from .views import (
    GameCategoryAPI,
    GameAPI
)


urlpatterns = [

    path('game_list/',GameCategoryAPI.as_view(),name='game-list'),
    path('<slug:game_slug>/',GameAPI.as_view(),name='game')
]