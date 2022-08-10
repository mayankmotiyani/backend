import re
from rest_framework import serializers
from blockchain.models import (
    Blockchain,
    BlockchainCategory,
    OurUnparalleledService,
    DummySection2,
    DummySection3,
    HeadingAndSubheading,
)


class HeadingAndSubheadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeadingAndSubheading
        fields = ['subheading','heading','description']

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
        fields = ['subheading','title','content','image']
    
     def to_representation(self, obj):
        instance = super(SingleBlockchainSerializer, self).to_representation(obj)
        instance['content'] = re.sub('\\t*\\r*\\n*\\\\*', '', instance['content'])
        return instance

class DummySection2Serializer(serializers.ModelSerializer):
    class Meta:
        model = DummySection2
        fields = ['subheading','title','content','image']
    
     def to_representation(self, obj):
        instance = super(SingleBlockchainSerializer, self).to_representation(obj)
        instance['content'] = re.sub('\\t*\\r*\\n*\\\\*', '', instance['content'])
        return instance
    
class DummySection3Serializer(serializers.ModelSerializer):
    class Meta:
        model = DummySection3
        fields = ['subheading','title','content','image']
    
     def to_representation(self, obj):
        instance = super(SingleBlockchainSerializer, self).to_representation(obj)
        instance['content'] = re.sub('\\t*\\r*\\n*\\\\*', '', instance['content'])
        return instance

class SingleBlockchainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blockchain
        fields = ['id','blockchain_description','blockchain_name']

    def to_representation(self, obj):
        instance = super(SingleBlockchainSerializer, self).to_representation(obj)
        return instance





        