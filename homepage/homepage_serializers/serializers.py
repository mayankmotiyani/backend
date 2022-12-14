from rest_framework import serializers
from homepage.models import (
    ProfessionalBlockchainDevelopmentCompany,
    Banner,
    WhyChooseUs,
    DevelopmentProcess,
    WhatWeDo,
    HeadingAndSubheading,
    BlockchainTechnology,
    BlogSection,
    TestimonialSection,
    Partner,
    ContactInformation,
    GetInTouch,
    Testimonial

)

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['client_name','client_feedback','image']

class ContactInformationAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInformation
        fields = "__all__"

class GetInTouchSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetInTouch
        fields = ['heading','description']

    def to_representation(self, obj):
        instance = super(GetInTouchSerializer, self).to_representation(obj)
        instance['contactInformation'] = ContactInformationAdminSerializer(ContactInformation.objects.first()).data
        return instance

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['id','image']

class BlockchainTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockchainTechnology
        fields = "__all__"
    
class BlogSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogSection
        fields = "__all__"

class TestimonialSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestimonialSection
        fields = ['id','subheading','content','image']


class HeadingAndSubheadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeadingAndSubheading
        fields = ['subheading','heading','description']

    # def to_representation(self, obj):
    #     instance = super(HeadingAndSubheadingSerializer,self).to_representation(obj)
    #     if instance['heading'] == "":
    #         del instance['heading']
    #     return instance

class ProfessionalBlockchainDevelopmentCompanySerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = ProfessionalBlockchainDevelopmentCompany
        fields = ["name","content","image_url"]

    def get_image_url(self, obj):
        return obj.image.url
    
    # def to_representation(self, obj):
    #     instance = super(OurMasterySerializer,self).to_representation(obj)
    #     instance['bool']=True
    #     return instance

class BannerSerializers(serializers.ModelSerializer):
    product_url = serializers.SerializerMethodField()
    class Meta:
        model = Banner
        fields = ["id","product","title","content","official_link","product_url","image"]
    
    def get_product_url(self,obj):
        return obj.get_absolute_url()
    
    def to_representation(self,obj):
        instance = super(BannerSerializers,self).to_representation(obj)
        instance['title'] = instance['title'].title()
        return instance

# class NotableBlockchainPlatformsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = NotableBlockchainPlatforms
#         fields = ['name','image','content']
    
class WhyChooseUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyChooseUs
        fields = ['service_name','icon','content']

class BlockchainDevelopmentProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevelopmentProcess
        fields = ["title","content","image"]

class WhatWeDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatWeDo
        fields = ['heading','title','content','image']

    
    # def to_representation(self, obj):
    #     instance = super(WhatWeDoSerializer, self).to_representation(obj)
    #     return instance