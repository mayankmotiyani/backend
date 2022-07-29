from django.urls import path
from .views import (
    PortfolioAPI
)

urlpatterns = [

    path('portfolio_list/',PortfolioAPI.as_view(),name='portfolio-list'),

]