from rest_framework import serializers
from product.models import (
    Product,
    Organization
)

class ProductSerializer(serializers.ModelSerializer):
    product_url = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['name','product_url']

    def get_product_url(self,obj):
        return obj.get_absolute_url()


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id',"name"]
    
    def to_representation(self, obj):
        instance = super(OrganizationSerializer,self).to_representation(obj)
        instance['array_of_product_list']=ProductSerializer(Product.objects.filter(organization_id=instance['id']),many=True).data
        return instance


    
    
        


