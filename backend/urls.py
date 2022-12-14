"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
""" 
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', TemplateView.as_view(template_name="index.html")),
    # re_path(r'^(?:.*)/?$',TemplateView.as_view(template_name="index.html")),
    path('api/',include('homepage.homepage_serializers.urls')),
    path('blockchain/',include('blockchain.blockchain_serializers.urls')),
    path('',include('talk_to_us.talk_to_us_serializers.urls')),
    path('game/',include('games.game_serializers.urls')),
    path('nft/',include('nft.nft_serializers.urls')),
    path('portfolio/',include('portfolio.portfolio_serializers.urls')),
    path('',include('company.company_serializers.urls')),
    path('blog/',include('blog.blog_serializers.urls')),
    path('about_us/',include('about_company.about_company_serializers.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('product/',include('product.product_serializers.urls')),
    path('resource/',include('resources.resource_serializers.urls')),
]

urlpatterns += static(settings.STATIC_URL,
                        document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)