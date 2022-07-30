from django.urls import path
from .views import (
    NftAPI,
    NftContentAPI
)


urlpatterns = [

    path('nft_list/',NftAPI.as_view(),name='nft-list'),
    path('<slug:nft_slug>/',NftContentAPI.as_view(),name='nft')
]