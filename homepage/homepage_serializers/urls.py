from django.urls import path
from .views import (
    OurMasteryAPI,
    HeroSectionAPI,
    WhyChooseUsAPI,
    BlockchainDevelopmentProcessAPI,
    WhatWeDoAPI,
    BlogSectionAPI,
    TestimonialSectionAPI,
    StartSomethingUndeniablyAPI,
    ProductAPI,
    GetInTouchAPI,
    TestimonialAPI
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
    path('testimonial/',TestimonialAPI.as_view(),name='testimonials'),
    path('possible-solution/',StartSomethingUndeniablyAPI.as_view(),name='possible-solution'),
    path('partner/',ProductAPI.as_view(),name='partner'),
    path('get-in-touch/',GetInTouchAPI.as_view(),name='get-in-touch')

]