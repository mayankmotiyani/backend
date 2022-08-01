from django.urls import path
from .views import (
    BlogAPI,
    SingleBlogAPI,
    BlogSearchAPI
)

urlpatterns = [
    path('blog_list/',BlogAPI.as_view()),
    path('<slug:blog_url>/',SingleBlogAPI.as_view(),name='blog'),
    path("blog_search/",BlogSearchAPI.as_view(),name='blog-search')
]   