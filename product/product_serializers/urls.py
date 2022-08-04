from django.urls import path
from .views import (
    ProductAPI,
    SingleProductAPI,
    OurGoalAPI,
    ProductPaymentMethodAPI,
    ProductFunctionalityAPI,
    AboutProductAPI
)

urlpatterns = [

    path('product_list/',ProductAPI.as_view()),
    path('<slug:product_url>/',SingleProductAPI.as_view(),name='product'),
    path('our-goal/<slug:product_url>/',OurGoalAPI.as_view(),name='product-goal'),
    path('payment-method/<slug:product_url>/',ProductPaymentMethodAPI.as_view(),name='payment-method'),
    path('payment-functionality/<slug:product_url>/',ProductFunctionalityAPI.as_view(),name='payment-functionality'),
    path('about-product/<slug:product_url>/',AboutProductAPI.as_view(),name='about-product'),

] 