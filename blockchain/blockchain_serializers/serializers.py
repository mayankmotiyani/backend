import re
from rest_framework import serializers
from blockchain.models import (
    Blockchain,
    BlockchainCategory,
    BlockchainService,
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

    
    # def to_representation(self, obj):
    #     instance = super(BlockChainSerializer, self).to_representation(obj)
    #     return instance

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
        # del instance['id']
        # del instance['blockchain_category']
        return instance
 
class SingleBlockchainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blockchain
        fields = ['blockchain_content']

    def to_representation(self, obj):
        instance = super(SingleBlockchainSerializer, self).to_representation(obj)
        instance['blockchain_content'] = re.sub('\\t*\\r*\\n*\\\\*', '', instance['blockchain_content'])
        return instance


# class BlockchainServiceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BlockchainService
#         fields = ['blockchain_service_name','blockchain_content','blockchain_service_slug']




        