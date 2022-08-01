from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.urls import reverse
from resources.models import (
    Resource
)

from .serializers import (
    ResourceSerializer
)

class ResourceAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_resources_instance = Resource.objects.all().order_by('created_at')
            serializer = ResourceSerializer(get_resources_instance,many=True)
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
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

class SingleResourceAPI(APIView):
    pass