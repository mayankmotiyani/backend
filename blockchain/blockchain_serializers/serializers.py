import re
from rest_framework import serializers
from blockchain.models import (
    Blockchain,
    BlockchainCategory,
    BlockchainService,
    OurUnparalleledService,
    DummySection2,
    DummySection3
)

class BlockChainSerializer(serializers.ModelSerializer):
    blockchain_api_url = serializers.SerializerMethodField()
    blockchain_url = serializers.SerializerMethodField()
    class Meta:
        model = Blockchain
        fields = ['blockchain_name','blockchain_slug','blockchain_url','blockchain_api_url']

    def get_blockchain_url(self, obj):
        return "/blockchain/" + obj.blockchain_slug + '/'

    def get_blockchain_api_url(self,obj):
        return obj.get_absolute_url()

class BlockChainCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockchainCategory
        fields = "__all__"

    def to_representation(self, obj):
        instance = super(BlockChainCategorySerializer,self).to_representation(obj)
        try:
            instance['array_of_blockchain_category_list'] = BlockChainSerializer(Blockchain.objects.filter(blockchainCategory__blockchain_category=instance['blockchain_category']),many=True).data
        except Exception as exception:
            pass
        return instance

class OurUnparalleledServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurUnparalleledService
        fields = ['title','content']

class DummySection2Serializer(serializers.ModelSerializer):
    class Meta:
        model = DummySection2
        fields = ['title','content']
    
class DummySection3Serializer(serializers.ModelSerializer):
    class Meta:
        model = DummySection3
        fields = ['title','content']


class SingleBlockchainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blockchain
        fields = ['id','blockchain_description']

    def to_representation(self, obj):
        instance = super(SingleBlockchainSerializer, self).to_representation(obj)
        instance['Section1'] = OurUnparalleledServiceSerializer(OurUnparalleledService.objects.get(blockchain_id=instance['id'])).data
        instance['Section2'] = DummySection2Serializer(DummySection2.objects.get(blockchain_id=instance['id'])).data
        instance['Section3'] = DummySection3Serializer(DummySection3.objects.get(blockchain_id=instance['id'])).data
        del instance['id']
        return instance





        