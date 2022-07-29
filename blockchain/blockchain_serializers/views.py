import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import F
from blockchain.models import(
    Blockchain,
    BlockchainCategory,
)

from .serializers import (
    BlockChainSerializer,
    BlockChainCategorySerializer,
    SingleBlockchainSerializer,
)

class BlockchainAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_blockchain_category = BlockchainCategory.objects.all().values("id","blockchain_category")
            get_list_of_blockchain_category = list(BlockchainCategory.objects.all().values_list("blockchain_category",flat=True))
            serializer = BlockChainCategorySerializer(get_blockchain_category,many=True)
            context ={
                "status":status.HTTP_200_OK,
                "success":True,
                "blockchain_category":get_list_of_blockchain_category,
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

class BlockChainContentAPI(APIView):
    def get(self, request, blockchain_slug, *args, **kwargs):
        try:
            get_blockchain_instance = Blockchain.objects.get(blockchain_slug__iexact = blockchain_slug)
            serializer = SingleBlockchainSerializer(get_blockchain_instance)
            context ={
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


class DashboardNichesAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_dashboard_niches_instance = DashboardNiches.objects.all()
            serializer = DashboardNichesSerializer(get_dashboard_niches_instance,many=True)
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



