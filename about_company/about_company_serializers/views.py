from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import F
from about_company.models import(
    ContactAddress,
    PrivacyPolicy,
    TermsAndCondition,
    AboutCompany,
    HeadingAndSubheading,
    UnmatchedServices,
    BlockchainForBusiness,
    VisionAndMission
)

from .serializers import (
    UnmatchedServicesSerializer,
    OfficeAddressSerializer,
    HeaderOfficeAddressSerializer,
    PrivacyPolicySerializer,
    TermsAndConditionSerializer,
    HeadingAndSubheadingSerializer,
    BlockchainForBusinessSerializer,
    VisionAndMissionSerializer
)

class UnmatchedServicesAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_about_section_instance = UnmatchedServices.objects.first()
            get_heading_and_subheading_serializer = HeadingAndSubheadingSerializer(HeadingAndSubheading.objects.get(id=get_about_section_instance.heading.id))
            serializer = UnmatchedServicesSerializer(get_about_section_instance)
            context ={
                "status":status.HTTP_200_OK,
                "success":True,
                "heading_and_subheading":get_heading_and_subheading_serializer.data,
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


class AboutAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_about_instance = AboutCompany.objects.first()
            serializer = AboutCompanySerializer(get_about_instance)
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

class TermAndConditionAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_term_and_condition_instance = TermsAndCondition.objects.all()
            serializer = TermsAndConditionSerializer(get_term_and_condition_instance,many=True)
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


class BlockchainForBusinessAPI(APIView):
    def get(self, request , *args, **kwargs):
        try:
            get_data = BlockchainForBusiness.objects.all()
            get_heading_subheading_instance = list(BlockchainForBusiness.objects.all().values_list("heading",flat=True).distinct())[0]
            get_heading_and_subheading_serializer = HeadingAndSubheadingSerializer(HeadingAndSubheading.objects.get(id=get_heading_subheading_instance))
            serializer = BlockchainForBusinessSerializer(get_data, many=True)
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
                "heading_and_subheading":get_heading_and_subheading_serializer.data,
                "response":serializer.data
            }
            return Response(context, status=status.HTTP_200_OK)
        except Exception as exception:
            context = {
                "status":status.HTTP_400_BAD_REQUEST,
                "success":False,
                "response":str(exception)
                }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

class VisionAndMissionAPI(APIView):
    def get(self, request , *args, **kwargs):
        try:
            get_data = VisionAndMission.objects.first()
            get_heading_and_subheading_serializer = HeadingAndSubheadingSerializer(HeadingAndSubheading.objects.get(id=get_data.heading.id))
            serializer = VisionAndMissionSerializer(get_data)
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
                "heading_and_subheading":get_heading_and_subheading_serializer.data,
                "response":serializer.data
            }
            return Response(context, status=status.HTTP_200_OK)
        except Exception as exception:
            context = {
                "status":status.HTTP_400_BAD_REQUEST,
                "success":False,
                "response":str(exception)
                }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        

class FrequentAskQuestionAPI(APIView):
    def get(self, request , *args, **kwargs):
        try:
            get_data = FAQs.objects.all()
            serializer = FAQsSerializer(get_data)
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
                "response":serializer.data
            }
            return Response(context, status=status.HTTP_200_OK)
        except Exception as exception:
            context = {
                "status":status.HTTP_400_BAD_REQUEST,
                "success":False,
                "response":str(exception)
                }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)