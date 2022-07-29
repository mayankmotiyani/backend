from django.urls import path
from .views import (
    OurMasteryAPI,
    HeroSectionAPI,
    NotableBlockchainPlatformsAPI
)

urlpatterns = [
    
    path("our-mastery/",OurMasteryAPI.as_view(),name="dashboard-niches"),
    path("hero-section-content/",HeroSectionAPI.as_view(),name="hero-section-content"),
    path("notable-blockchain-platform/",NotableBlockchainPlatformsAPI.as_view(),name="notable-blockchain-platform")

]