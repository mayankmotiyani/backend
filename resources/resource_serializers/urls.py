from django.urls import path
from .views import (
    ResourceAPI,
    SingleResourceAPI
)

urlpatterns = [
    path('resources_list/',ResourceAPI.as_view()),
    path('<slug:resource_url>/',SingleResourceAPI.as_view(),name='resource'),
]