from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (
    ProductSerializer,
    OrganizationSerializer
)
from product.models import (
    Product,
    Organization
)
from rest_framework import (
    status
)


class ProductAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_organization_instance = Organization.objects.all()
            serializer = OrganizationSerializer(get_organization_instance,many=True)
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
                "response":serializer.data
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

class SingleProductAPI(APIView):
    pass