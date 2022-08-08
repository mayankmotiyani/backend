from django.urls import path
from .views import (
    TeamAPI,
    GetCompanyModelsAPI,
    CareerAPI,
    SingleCareerAPI,
    ApplyForJobViewSet
)
urlpatterns = [

    path('team/',TeamAPI.as_view(),name='team-members'),
    path('career/',CareerAPI.as_view()),
    path('career/<slug:career_slug>/',SingleCareerAPI.as_view(),name='career'),
    path('get-all-models/',GetCompanyModelsAPI.as_view(),name='get-all-models-from-company'),
    path('apply-job/<slug:career_slug>/',ApplyForJobViewSet.as_view({'post': 'create'}),name='apply-for-job')
    
]