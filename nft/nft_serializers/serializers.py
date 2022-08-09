import re
from rest_framework import serializers
from nft.models import (
    NFT,
    NFTUseCases,
    NFTMarketplaceDevelopmentService,
    HeadingAndSubheading,
    NFTSection2
)

class HeadingAndSubheadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeadingAndSubheading
        fields = ['subheading','heading','description']

class NftSerializer(serializers.ModelSerializer):
    nft_url = serializers.SerializerMethodField()
    class Meta:
        model = NFT
        fields = ['name','nft_url']
    
    def get_nft_url(self,obj):
        return obj.get_absolute_url()

class NFTSection2Serializer(serializers.ModelSerializer):
    class Meta:
        model = NFTSection2
        fields = "__all__"
    
    # def to_representation(self, obj):
    #     instance = super(NFTSection2Serializer, self).to_representation(obj)

        
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
        fields = ['id','name','description']
    
    def to_representation(self, obj):
        instance = super(SingleNFTSerializer, self).to_representation(obj)
        instance['Section1'] = NFTMarketplaceDevelopmentServiceSerializer(NFTMarketplaceDevelopmentService.objects.filter(nft_id=instance['id']),many=True).data
        instance['Section2'] = list(NFTUseCases.objects.filter(nft_id=instance['id']).values_list('content',flat=True))
        instance['Section3'] = NFTUseCasesSerializer(NFTUseCases.objects.filter(nft_id=instance['id']),many=True).data
        del instance['id']
        return instance