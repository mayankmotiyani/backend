from django.urls import path
from .views import (
    TeamAPI,
    GetCompanyModelsAPI,
    TestimonialAPI,
    CareerAPI,
    SingleCareerAPI,
)
urlpatterns = [

    path('team/',TeamAPI.as_view(),name='team-members'),
    path('testimonial/',TestimonialAPI.as_view(),name='testimonial'),
    path('career/',CareerAPI.as_view()),
    path('career/<slug:career_slug>/',SingleCareerAPI.as_view(),name='career'),
    path('get-all-models/',GetCompanyModelsAPI.as_view(),name='get-all-models-from-company')
    
]