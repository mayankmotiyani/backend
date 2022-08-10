from django.urls import path
from .views import (
    AboutAPI,
    OfficeAddressAPI,
    HeaderOfficeAddressAPI,
    PrivacyPolicyAPI,
    TermAndConditionAPI,
    BlockchainForBusinessAPI,
    UnmatchedServicesAPI,
    VisionAndMissionAPI,
    FrequentAskQuestionAPI
)

urlpatterns = [
    path('',AboutAPI.as_view(),name='about-us'),
    path('hero-section/',UnmatchedServicesAPI.as_view(),name='about-main-section'),
    path('office-address/',OfficeAddressAPI.as_view()),
    path('header-office-address/',HeaderOfficeAddressAPI.as_view()),
    path('privacy-policy/',PrivacyPolicyAPI.as_view()),
    path('term-and-condition/',TermAndConditionAPI.as_view()),
    path('blockchain-for-business/',BlockchainForBusinessAPI.as_view(),name='blockchain-for-business'),
    path('vision-and-mission/',VisionAndMissionAPI.as_view(),name='vision-and-mission'),
    path('faq/',FrequentAskQuestionAPI.as_view(),name='faq'),
    
    

]