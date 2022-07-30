import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from nft.models import (
    NFT
)

from .serializers import (
    NftSerializer
)

class NftAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_games = NFT.objects.all()
            serializer = NftSerializer(get_games,many=True)
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
        
class NftContentAPI(APIView):
    pass