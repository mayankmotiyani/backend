from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import F
from homepage.models import (
    OurMastery,
    HeroSection,
    NotableBlockchainPlatforms,
    WhyChooseUs,
    DevelopmentProcess
)

from .serializers import (
    OurMasterySerializer,
    HeroSectionSerializers,
    NotableBlockchainPlatformsSerializer,
    WhyChooseUsSerializer,
    BlockchainDevelopmentProcessSerializer

)
class OurMasteryAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_dashboard_niches_instance = OurMastery.objects.all()
            serializer = OurMasterySerializer(get_dashboard_niches_instance,many=True)
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
    
class HeroSectionAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_hero_section_instance = HeroSection.objects.all()
            serializer = HeroSectionSerializers(get_hero_section_instance,many=True)
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


class NotableBlockchainPlatformsAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_notable_blockchain_platform = NotableBlockchainPlatforms.objects.all()
            serializer = NotableBlockchainPlatformsSerializer(get_notable_blockchain_platform,many=True)
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
    

class WhyChooseUsAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_why_we_choose_instance = WhyChooseUs.objects.all()
            serializer = WhyChooseUsSerializer(get_why_we_choose_instance, many=True)
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

class BlockchainDevelopmentProcessAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_blockchain_process_instance = DevelopmentProcess.objects.all().order_by('created_at')
            serializer = BlockchainDevelopmentProcessSerializer(get_blockchain_process_instance, many=True)
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