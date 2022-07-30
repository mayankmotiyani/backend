import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from games.models import (
    Game
)

from .serializers import (
    GameSerializer
)


class GameAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_games = Game.objects.all()
            serializer = GameSerializer(get_games,many=True)
            # games = json.loads(json.dumps(serializer.data))
            # list_of_games = [game['name'] for game in games]
        
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
    pass