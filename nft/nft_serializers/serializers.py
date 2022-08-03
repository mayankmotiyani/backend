from rest_framework import serializers
from nft.models import (
    NFT,
    NFTUseCases,
    NFTMarketplaceDevelopmentService
)

class NftSerializer(serializers.ModelSerializer):
    nft_url = serializers.SerializerMethodField()
    class Meta:
        model = NFT
        fields = ['name','nft_url']
    
    def get_nft_url(self,obj):
        return obj.get_absolute_url()
        
class NFTUseCasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFTUseCases
        fields = "__all__"

class NFTMarketplaceDevelopmentServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFTMarketplaceDevelopmentService
        fields = "__all__"


class SingleNFTSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFT
        fields = ['id','description']
    
    def to_representation(self, obj):
        instance = super(SingleNFTSerializer, self).to_representation(obj)
        instance['Section1'] = NFTMarketplaceDevelopmentServiceSerializer(NFTMarketplaceDevelopmentService.objects.get(nft_id=instance['id'])).data
        instance['Section2'] = NFTUseCasesSerializer(NFTUseCases.objects.get(nft_id=instance['id'])).data
        del instance['id']
        return instance