from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import F
from homepage.models import (
    ProfessionalBlockchainDevelopmentCompany,
    Banner,
    WhyChooseUs,
    DevelopmentProcess,
    WhatWeDo,
    HeadingAndSubheading,
    BlockchainTechnology,
    BlogSection,
    TestimonialSection,
    Partner,
    GetInTouch,
    Testimonial
)

from .serializers import (
    ProfessionalBlockchainDevelopmentCompanySerializer,
    BannerSerializers,
    WhyChooseUsSerializer,
    BlockchainDevelopmentProcessSerializer,
    WhatWeDoSerializer,
    HeadingAndSubheadingSerializer,
    BlockchainTechnologySerializer,
    BlogSectionSerializer,
    TestimonialSectionSerializer,
    PartnerSerializer,
    GetInTouchSerializer ,
    TestimonialSerializer

)

class BlogSectionAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_blog_section_instance = BlogSection.objects.first()
            serializer = BlogSectionSerializer(get_blog_section_instance)
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

class TestimonialSectionAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_testimonial_section_instance = TestimonialSection.objects.first()
            serializer = TestimonialSectionSerializer(get_testimonial_section_instance)
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

class BlockchainTechnologySerializerAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_undeniable_section_instance = BlockchainTechnology.objects.first()
            serializer = BlockchainTechnologySerializer(get_undeniable_section_instance)
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


class ProfessionalBlockchainDevelopmentCompanyAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_dashboard_niches_instance = ProfessionalBlockchainDevelopmentCompany.objects.all()
            get_heading_and_subheading = list(ProfessionalBlockchainDevelopmentCompany.objects.all().values_list("heading_and_subheading_id",flat=True).distinct())[0]
            get_heading_and_subheading_serializer = HeadingAndSubheadingSerializer(HeadingAndSubheading.objects.get(id=get_heading_and_subheading))
            serializer = ProfessionalBlockchainDevelopmentCompanySerializer(get_dashboard_niches_instance,many=True)
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
            get_hero_section_instance = Banner.objects.all()
            # get_heading_and_subheading = list(HeroSection.objects.all().values_list("heading_and_subheading_id",flat=True).distinct())[0]
            # get_heading_and_subheading_serializer = HeadingAndSubheadingSerializer(HeadingAndSubheading.objects.get(id=get_heading_and_subheading))
            serializer = BannerSerializers(get_hero_section_instance,many=True)
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

class ProductAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_partner_instance = Partner.objects.all()
            serializer = PartnerSerializer(get_partner_instance,many=True)
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

class GetInTouchAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_get_in_touch_instance = GetInTouch.objects.first()
            serializer = GetInTouchSerializer(get_get_in_touch_instance)
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

class TestimonialAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_testimonial = Testimonial.objects.all()
            serializer = TestimonialSerializer(get_testimonial,many=True)
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