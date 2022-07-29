from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    PortfolioSerializer
)
from portfolio.models import (
    Portfolio
)
class PortfolioAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_portfolio = Portfolio.objects.all()
            serializer = PortfolioSerializer(get_portfolio,many=True)
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