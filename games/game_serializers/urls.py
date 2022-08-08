from django.urls import path
from .views import (
    GameAPI,
    GameContentAPI,
    GameSection2API,
    GameSection1API
)


urlpatterns = [

    path('game_list/',GameAPI.as_view(),name='game-list'),
    path('<slug:game_slug>/',GameContentAPI.as_view(),name='game'),
    path('game-section-1/<slug:game_slug>/',GameSection1API.as_view(),name='game-section-1'),
    path('game-section-2/<slug:game_slug>/',GameSection2API.as_view(),name='game-section-2')
    
]