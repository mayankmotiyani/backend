from django.urls import path
from .views import (
    NftAPI
)


urlpatterns = [

    path('nft_list/',NftAPI.as_view(),name='nft-list')
]