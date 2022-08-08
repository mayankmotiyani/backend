from django.urls import path
from .views import (
    NftAPI,
    NftContentAPI,
    NftSection1API,
    NftSection2API,
    NftSection3API
)


urlpatterns = [

    path('nft_list/',NftAPI.as_view(),name='nft-list'),
    path('<slug:nft_slug>/',NftContentAPI.as_view(),name='nft'),
    path('nft-section-1/<slug:nft_slug>/',NftSection1API.as_view(),name='nft-section-1'),
    path('nft-section-2/<slug:nft_slug>/',NftSection2API.as_view(),name='nft-section-2'),
    path('nft-section-3/<slug:nft_slug>/',NftSection3API.as_view(),name='nft-section-3'),
]