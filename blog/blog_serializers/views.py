from rest_framework.views import APIView
from rest_framework.response import Response
from blog.models import (
    Blog
)
from .serializers import (
    BlogSerializer,
    SingleBlogSerializer
)

from rest_framework import (
    generics,
    filters,
    status,
)



class BlogAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_blog_instance = Blog.objects.all().order_by('created_at')[:4]
            serializer = BlogSerializer(get_blog_instance,many=True)
            blog_list = list(Blog.objects.all().values_list("title",flat=True))
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
                "blog_list":blog_list,
                "response":serializer.data
            }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as exception:
            context = {
                "status":status.HTTP_400_BAD_REQUEST,
                "success":False,
                "response":str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

class SingleBlogAPI(APIView):
    def get(self, request, blog_url, *args, **kwargs):
        try:
            get_blog_instance = Blog.objects.get(slug=blog_url)
            serializer = SingleBlogSerializer(get_blog_instance)
            blog_list = list(Blog.objects.exclude(slug=blog_url).values_list("title",flat=True))
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
                "blog_list":blog_list,
                "response":serializer.data
            }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as exception:
            context = {
                "status":status.HTTP_400_BAD_REQUEST,
                "success":False,
                "response":str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

class BlogSearchAPI(generics.ListCreateAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

 