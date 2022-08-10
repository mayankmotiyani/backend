import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from games.models import (
    Game,
    GameSection2,
    HeadingAndSubheading,
    ModernSolutionForVariousPlatform,
    GameSection3,
    GamePartner
)

from .serializers import (
    GameSerializer,
    SingleGameSerializer,
    GameSection2Serializer,
    HeadingAndSubheadingSerializer,
    ModernSolutionForVariousPlatformSerializer,
    GameSection3Serializer,
    GamePartnerSerializer
)




class GameAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_games = Game.objects.all()
            serializer = GameSerializer(get_games,many=True)
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
                "response": serializer.data
            }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as exception:
            context = {
                "status":status.HTTP_400_BAD_REQUEST,
                "success":False,
                "response":str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)
        
    
class GameContentAPI(APIView):
    def get(self, request, game_slug, *args, **kwargs):
        try:
            get_games = Game.objects.get(slug=game_slug)
            serializer = SingleGameSerializer(get_games)
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
                "response": serializer.data
            }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as exception:
            context = {
                "status":status.HTTP_400_BAD_REQUEST,
                "success":False,
                "response":str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

            
class GameSection1API(APIView):
    def get(self, request,game_slug, *args, **kwargs):
        try:
            get_game_section_1_instance = ModernSolutionForVariousPlatform.objects.get(game__slug=game_slug)
            serializer = ModernSolutionForVariousPlatformSerializer(get_game_section_1_instance)
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
                "response": serializer.data
            }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as exception:
            context = {
                "status":status.HTTP_400_BAD_REQUEST,
                "success":False,
                "response":str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

class GameSection2API(APIView):
    def get(self, request,game_slug, *args, **kwargs):
        try:
            get_game_section_2_instance = GameSection2.objects.filter(game__slug=game_slug)
            get_heading_and_subheading = list(GameSection2.objects.filter(game__slug=game_slug).values_list("heading_id",flat=True).distinct())[0]

            get_heading_and_subheading_serializer = HeadingAndSubheadingSerializer(HeadingAndSubheading.objects.get(id=get_heading_and_subheading))
            serializer = GameSection2Serializer(get_game_section_2_instance,many=True)
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
                "heading_and_subheading":get_heading_and_subheading_serializer.data,
                "response": serializer.data
            }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as exception:
            context = {
                "status":status.HTTP_400_BAD_REQUEST,
                "success":False,
                "response":str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

class GameSection3API(APIView):
    def get(self, request,game_slug, *args, **kwargs):
        try:
            get_game_section_3_instance = GameSection3.objects.filter(game__slug=game_slug)
            serializer = GameSection3Serializer(get_game_section_3_instance,many=True)
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
                "response": serializer.data
            }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as exception:
            context = {
                "status":status.HTTP_400_BAD_REQUEST,
                "success":False,
                "response":str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

class GamePartnerAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_game_partners_instance = GamePartner.objects.all()
            get_heading_and_subheading = list(GamePartner.objects.all().values_list("heading_id",flat=True).distinct())[0]
            get_heading_and_subheading_serializer = HeadingAndSubheadingSerializer(HeadingAndSubheading.objects.get(id=get_heading_and_subheading))
            serializer = GamePartnerSerializer(get_game_partners_instance,many=True)
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
                "heading_and_subheading":get_heading_and_subheading_serializer.data,
                "response": serializer.data
            }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as exception:
            context = {
                "status":status.HTTP_400_BAD_REQUEST,
                "success":False,
                "response":str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)