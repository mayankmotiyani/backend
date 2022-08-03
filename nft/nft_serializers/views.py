import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from nft.models import (
    NFT
)

from .serializers import (
    NftSerializer,
    SingleNFTSerializer
)

class NftAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_nft = NFT.objects.all()
            serializer = NftSerializer(get_nft,many=True)
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
    def get(self, request, nft_slug, *args, **kwargs):
        try:
            get_nft = NFT.objects.get(slug=nft_slug)
            serializer = SingleNFTSerializer(get_nft)
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