from rest_framework import serializers
from nft.models import (
    NFT
)

class NftSerializer(serializers.ModelSerializer):
    nft_url = serializers.SerializerMethodField()
    class Meta:
        model = NFT
        fields = ['name','nft_url']
    
    def get_nft_url(self,obj):
        return obj.get_absolute_url()
        
        