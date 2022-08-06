import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import F
from blockchain.models import(
    Blockchain,
    BlockchainCategory,
    OurUnparalleledService,
    DummySection2,
    DummySection3
)

from .serializers import (
    BlockChainSerializer,
    BlockChainCategorySerializer,
    SingleBlockchainSerializer,
    OurUnparalleledServiceSerializer,
    DummySection2Serializer,
    DummySection3Serializer
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


class BlockchainSectionOneAPI(APIView):
    def get(self, request, blockchain_slug, *args, **kwargs):
        try:
            get_blockchain_instance = Blockchain.objects.get(blockchain_slug=blockchain_slug)
            get_blockchain_section_one_instance = OurUnparalleledService.objects.get(blockchain_id=get_blockchain_instance.id)
            serializer = OurUnparalleledServiceSerializer(get_blockchain_section_one_instance)
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


class BlockchainSectionTwoAPI(APIView):
    def get(self, request, blockchain_slug, *args, **kwargs):
        try:
            get_blockchain_instance = Blockchain.objects.get(blockchain_slug=blockchain_slug)
            get_blockchain_section_two_instance = DummySection2.objects.get(blockchain_id=get_blockchain_instance.id)
            serializer = DummySection2Serializer(get_blockchain_section_two_instance)
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


class BlockchainSectionThreeAPI(APIView):
    def get(self, request, blockchain_slug, *args, **kwargs):
        try:
            get_blockchain_instance = Blockchain.objects.get(blockchain_slug=blockchain_slug)
            get_blockchain_section_third_instance = DummySection3.objects.get(blockchain_id=get_blockchain_instance.id)
            serializer = DummySection3Serializer(get_blockchain_section_third_instance)
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
