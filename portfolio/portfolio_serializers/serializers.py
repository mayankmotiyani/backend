from rest_framework import serializers
from portfolio.models import (
    Portfolio
)

class PortfolioSerializer(serializers.ModelSerializer):
    portfolio_name = serializers.SerializerMethodField()
    class Meta:
        model = Portfolio
        fields = ['name','portfolio_name','image']

    def get_portfolio_name(self,obj):
        return obj.name.upper()
