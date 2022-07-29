from rest_framework import serializers
from nft.models import (
    NFT
)

class NftSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFT
        fields = ['name']
        
        