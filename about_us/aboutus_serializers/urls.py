from django.urls import path
from .views import (
    AboutAPI,
    OfficeAddressAPI,
    HeaderOfficeAddressAPI

)

urlpatterns = [
    
    path('about_us_list/',AboutAPI.as_view(),name='About_us_list'),
    path('office-address/',OfficeAddressAPI.as_view()),
    path('header-office-address/',HeaderOfficeAddressAPI.as_view())
    
    

]