from rest_framework import serializers
from product.models import (
    Product,
    Organization,
    OurGoal,
    ProductPaymentMethod,
    HeadingAndSubheading,
    ProductFunctionality,
    AboutProduct,
    ProductSolutionImage,
    ProductSolutionContent,
    ProductOutComeImage,
    ProductOutComeContent
)

class ProductSolutionContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSolutionContent
        fields = ['title','content']

class ProductOutComeContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSolutionContent
        fields = ['title','content']

class AboutProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutProduct
        fields = ['title','content','image']

class HeadingAndSubheadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeadingAndSubheading
        fields = ['subheading','heading','description']

    # def to_representation(self, obj):
    #     instance = super(HeadingAndSubheadingSerializer,self).to_representation(obj)
    #     if instance['heading'] == "":
    #         del instance['heading']
    #     return instance

class OurGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurGoal
        fields = ['title','content']


class ProductPaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPaymentMethod
        fields = ['title','content']


class ProductFunctionalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFunctionality
        fields = ['title','content']

    # def to_representation(self, obj):
    #     instance = super(ProductPaymentMethodSerializer,self).to_representation(obj)
    #     return instance

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


    
    
        


