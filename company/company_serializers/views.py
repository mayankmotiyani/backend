from asyncio import exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.apps import apps
from company.models import (
    Team,
    Testimonial,
    Careers,
    ApplyForJob
    
    
)
from .serializers import (
    TeamSerializer,
    TestimonialSerializer,
    CareerSerializer,
    SingleCareerSerializer,
    ApplyForJobSerializer
   
)
from rest_framework import viewsets

class GetCompanyModelsAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            company_dict = {}
            get_all_models_from_company = [i.__name__ for i in apps.all_models['company'].values()]
            company_dict['Company'] = get_all_models_from_company
            company_dict['Services'] = ['Node JS Development','PHP Website Development','CakePHP Development','WordPress Development'] 
            company_dict['About'] = ['About Company','Vision & Mission','Become Our Partner','Our Technology Partners']
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
                "response":company_dict
            }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as exception:
            context = {
                "status":status.HTTP_400_BAD_REQUEST,
                "success":False,
                "response":str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

class TeamAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_team_members = Team.objects.all().order_by('member_unique_id')
            serializer = TeamSerializer(get_team_members,many=True)
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
        
class CareerAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_career = Careers.objects.filter(opening_available=True,opening__gt = 0)
            serializer = CareerSerializer(get_career,many=True)
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
        
        
class SingleCareerAPI(APIView):
    def get(self, request, career_slug, *args, **kwargs):
        try:
            get_career = Careers.objects.get(slug=career_slug)
            serializer = SingleCareerSerializer(get_career)
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

            
class ApplyForJobViewSet(viewsets.ModelViewSet):
    serializer_class = ApplyForJobSerializer

    def create(self, request,career_slug,*args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            get_job_profile_instance = Careers.objects.get(slug=career_slug)
            if serializer.is_valid():
                serializer.save(job_profile=get_job_profile_instance.opening_designation)
                content = {
                    "status":status.HTTP_200_OK,
                    "success":True,
                    "response":"Thanks for applying!"
                }
                return Response(content, status=status.HTTP_201_CREATED)
            else:
                content = {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "success":False,
                    "response": serializer.errors,
                }
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
        except Exception as exception:
            context = {
                "status":status.HTTP_400_BAD_REQUEST,
                "success":False,
                "response":str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)
