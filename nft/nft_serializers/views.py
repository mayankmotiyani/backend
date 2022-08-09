import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from nft.models import (
    NFT,
    NFTMarketplaceDevelopmentService,
    HeadingAndSubheading,
    NFTUseCases,
    NFTSection2
)

from .serializers import (
    NftSerializer,
    SingleNFTSerializer,
    NFTMarketplaceDevelopmentServiceSerializer,
    HeadingAndSubheadingSerializer,
    NFTUseCasesSerializer,
    NFTSection2Serializer
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

class NftSection1API(APIView):
    def get(self, request,nft_slug, *args, **kwargs):
        try:
            get_nft = NFTMarketplaceDevelopmentService.objects.filter(nft__slug=nft_slug)
            get_heading_and_subheading = list(NFTMarketplaceDevelopmentService.objects.filter(nft__slug=nft_slug).values_list("heading_id",flat=True).distinct())[0]
            get_heading_and_subheading_serializer = HeadingAndSubheadingSerializer(HeadingAndSubheading.objects.get(id=get_heading_and_subheading))
            serializer = NFTMarketplaceDevelopmentServiceSerializer(get_nft,many=True)
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
    
class NftSection2API(APIView):
    def get(self, request,nft_slug, *args, **kwargs):
        try:
            get_nft = NFTSection2.objects.get(nft__slug=nft_slug)
            serializer = NFTSection2Serializer(get_nft)
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
    
class NftSection3API(APIView):
    def get(self, request,nft_slug, *args, **kwargs):
        try:
            get_nft = NFTUseCases.objects.filter(nft__slug=nft_slug)
            get_heading_and_subheading = list(NFTUseCases.objects.filter(nft__slug=nft_slug).values_list("heading_id",flat=True).distinct())[0]
            get_heading_and_subheading_serializer = HeadingAndSubheadingSerializer(HeadingAndSubheading.objects.get(id=get_heading_and_subheading))
            serializer = NFTUseCasesSerializer(get_nft,many=True)
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