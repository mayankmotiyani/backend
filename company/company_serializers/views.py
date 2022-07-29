from asyncio import exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.apps import apps
from company.models import (
    Team,
    Testimonial,
    Careers
    
    
)
from .serializers import (
    TeamSerializer,
    TestimonialSerializer,
    CareerSerializer,
   
)

class GetCompanyModelsAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            company_dict = {}
            get_all_models_from_company = [i.__name__ for i in apps.all_models['company'].values()]
            company_dict['Company'] = get_all_models_from_company
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
            get_career = Careers.objects.all()
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
        
        

            
            