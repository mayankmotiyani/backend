from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import F
from about_company.models import(
    About,
    ContactAddress,
    PrivacyPolicy
)

from .serializers import (
    AboutUsSerializer,
    OfficeAddressSerializer,
    HeaderOfficeAddressSerializer,
    PrivacyPolicySerializer
   
)


class AboutAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_about_category = About.objects.all().values("id","name","image")
            serializer = AboutUsSerializer(get_about_category,many=True)
            context ={
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

class OfficeAddressAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_office_address_instance = ContactAddress.objects.exclude(office__icontains = "india")
            excluded_serializer = OfficeAddressSerializer(get_office_address_instance,many=True)
            get_office_address_india_instance = ContactAddress.objects.get(office__icontains = "india")
            serializer = OfficeAddressSerializer(get_office_address_india_instance)
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
                "infograins_india_office":serializer.data, 
                "response":excluded_serializer.data,
            }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as exception:
            context = {
                "status":status.HTTP_400_BAD_REQUEST,
                "success":False,
                "response":str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)
            
class HeaderOfficeAddressAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_contact_address_instance = ContactAddress.objects.all()
            serializer = HeaderOfficeAddressSerializer(get_contact_address_instance,many=True)
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

class PrivacyPolicyAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_privacy_policy_instance = PrivacyPolicy.objects.all()
            serializer = PrivacyPolicySerializer(get_privacy_policy_instance,many=True)
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
