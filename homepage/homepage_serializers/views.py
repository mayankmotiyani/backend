from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import F
from homepage.models import (
    OurMastery,
    HeroSection,
    WhyChooseUs,
    DevelopmentProcess,
    WhatWeDo,
    HeadingAndSubheading
)

from .serializers import (
    OurMasterySerializer,
    HeroSectionSerializers,
    WhyChooseUsSerializer,
    BlockchainDevelopmentProcessSerializer,
    WhatWeDoSerializer,
    HeadingAndSubheadingSerializer

)


class OurMasteryAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_dashboard_niches_instance = OurMastery.objects.all()
            get_heading_and_subheading = list(OurMastery.objects.all().values_list("heading_and_subheading_id",flat=True).distinct())[0]
            get_heading_and_subheading_serializer = HeadingAndSubheadingSerializer(HeadingAndSubheading.objects.get(id=get_heading_and_subheading))
            serializer = OurMasterySerializer(get_dashboard_niches_instance,many=True)
            context = {
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
    
class HeroSectionAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_hero_section_instance = HeroSection.objects.all()
            # get_heading_and_subheading = list(HeroSection.objects.all().values_list("heading_and_subheading_id",flat=True).distinct())[0]
            # get_heading_and_subheading_serializer = HeadingAndSubheadingSerializer(HeadingAndSubheading.objects.get(id=get_heading_and_subheading))
            serializer = HeroSectionSerializers(get_hero_section_instance,many=True)
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
                # "heading_and_subheading":get_heading_and_subheading_serializer.data,
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


# class NotableBlockchainPlatformsAPI(APIView):
#     def get(self, request, *args, **kwargs):
#         try:
#             get_notable_blockchain_platform = NotableBlockchainPlatforms.objects.all()
#             get_heading_and_subheading = list(NotableBlockchainPlatforms.objects.all().values_list("heading_and_subheading_id",flat=True).distinct())[0]
#             get_heading_and_subheading_serializer = HeadingAndSubheadingSerializer(HeadingAndSubheading.objects.get(id=get_heading_and_subheading))
#             serializer = NotableBlockchainPlatformsSerializer(get_notable_blockchain_platform,many=True)
#             context = {
#                 "status":status.HTTP_200_OK,
#                 "success":True,
#                 "heading_and_subheading":get_heading_and_subheading_serializer.data,
#                 "response":serializer.data
#             }
#             return Response(context,status=status.HTTP_200_OK)
#         except Exception as exception:
#             context = {
#                 "status":status.HTTP_400_BAD_REQUEST,
#                 "success":False,
#                 "response":str(exception)
#             }
#             return Response(context,status=status.HTTP_400_BAD_REQUEST)
    

class WhyChooseUsAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_why_we_choose_instance = WhyChooseUs.objects.all()
            get_heading_and_subheading = list(WhyChooseUs.objects.all().values_list("heading_and_subheading_id",flat=True).distinct())[0]
            get_heading_and_subheading_serializer = HeadingAndSubheadingSerializer(HeadingAndSubheading.objects.get(id=get_heading_and_subheading))
            serializer = WhyChooseUsSerializer(get_why_we_choose_instance, many=True)
            context = {
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

class BlockchainDevelopmentProcessAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_blockchain_process_instance = DevelopmentProcess.objects.all().order_by('created_at')
            get_heading_and_subheading = list(DevelopmentProcess.objects.all().values_list("heading_and_subheading_id",flat=True).distinct())[0]
            get_heading_and_subheading_serializer = HeadingAndSubheadingSerializer(HeadingAndSubheading.objects.get(id=get_heading_and_subheading))
            serializer = BlockchainDevelopmentProcessSerializer(get_blockchain_process_instance, many=True)
            context = {
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

class WhatWeDoAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_what_we_do_instance = WhatWeDo.objects.all()
            serializer = WhatWeDoSerializer(get_what_we_do_instance,many=True)
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