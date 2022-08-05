from django.urls import path
from .views import (
    AboutAPI,
    OfficeAddressAPI,
    HeaderOfficeAddressAPI,
    PrivacyPolicyAPI,
    TermAndConditionAPI,
    AboutCompanySection1API
)

urlpatterns = [
    path('',AboutAPI.as_view(),name='about-us'),
    path('hero-section/',AboutCompanySection1API.as_view(),name='about-main-section'),
    path('office-address/',OfficeAddressAPI.as_view()),
    path('header-office-address/',HeaderOfficeAddressAPI.as_view()),
    path('privacy-policy/',PrivacyPolicyAPI.as_view()),
    path('term-and-condition/',TermAndConditionAPI.as_view()),
    
    

]