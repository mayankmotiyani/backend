from django.urls import path
from .views import (
    BlockchainAPI,
    BlockChainContentAPI,
    BlockchainSectionOneAPI,
    BlockchainSectionTwoAPI,
    BlockchainSectionThreeAPI
    
)

urlpatterns = [
    
    path('blockchain_list/',BlockchainAPI.as_view(),name='blockchain-list'),
    path('<slug:blockchain_slug>/',BlockChainContentAPI.as_view(),name='blockchain'),
    path('blockchain-section-one/<slug:blockchain_slug>/',BlockchainSectionOneAPI.as_view(),name='blockchain-section-one'),
    path('blockchain-section-two/<slug:blockchain_slug>/',BlockchainSectionTwoAPI.as_view(),name='blockchain-section-two'),
    path('blockchain-section-three/<slug:blockchain_slug>/',BlockchainSectionThreeAPI.as_view(),name='blockchain-section-three')

]