from django.urls import path
from .views import (
    OurMasteryAPI,
    HeroSectionAPI,
    WhyChooseUsAPI,
    BlockchainDevelopmentProcessAPI,
    WhatWeDoAPI,
    BlogSectionAPI,
    TestimonialSectionAPI,
    StartSomethingUndeniablyAPI
)

urlpatterns = [
    
    path("our-mastery/",OurMasteryAPI.as_view(),name="dashboard-niches"),
    path("hero-section-content/",HeroSectionAPI.as_view(),name="hero-section-content"),
    # path("notable-blockchain-platform/",NotableBlockchainPlatformsAPI.as_view(),name="notable-blockchain-platform"),
    path('why-we-choose/',WhyChooseUsAPI.as_view(),name='why-we-choose'),
    path('blockchain-development-process/',BlockchainDevelopmentProcessAPI.as_view()),
    path('what-we-do/',WhatWeDoAPI.as_view(),name='what-we-do'),
    path('blog-section/',BlogSectionAPI.as_view(),name='blog-section'),
    path('testimonials-section/',TestimonialSectionAPI.as_view(),name='testimonials-section'),
    path('possible-solution/',StartSomethingUndeniablyAPI.as_view(),name='possible-solution'),

]