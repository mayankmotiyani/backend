from django.urls import path
from .views import (
    TeamAPI,
    GetCompanyModelsAPI,
    TestimonialAPI,
    CareerAPI
)
urlpatterns = [

    path('team-members/',TeamAPI.as_view(),name='team-members'),
    path('testimonial/',TestimonialAPI.as_view(),name='testimonial'),
    path('careers/',CareerAPI.as_view(),name='careers'),
    path('get-all-models/',GetCompanyModelsAPI.as_view(),name='get-all-models-from-company')
    
]