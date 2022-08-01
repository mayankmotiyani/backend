from django.urls import path
from .views import (
    ProductAPI,
    SingleProductAPI,

)

urlpatterns = [

    path('product_list/',ProductAPI.as_view()),
    path('<slug:product_url>/',SingleProductAPI.as_view(),name='product'),

] 