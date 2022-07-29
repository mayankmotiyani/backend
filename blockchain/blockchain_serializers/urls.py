from django.urls import path
from .views import (
    BlockchainAPI,
    BlockChainContentAPI,
    
)

urlpatterns = [
    
    path('blockchain_list/',BlockchainAPI.as_view(),name='blockchain-list'),
    path('<slug:blockchain_slug>/',BlockChainContentAPI.as_view(),name='blockchain'),

]