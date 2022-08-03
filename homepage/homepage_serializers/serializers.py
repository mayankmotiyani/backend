from rest_framework import serializers
from homepage.models import (
    OurMastery,
    HeroSection,
    NotableBlockchainPlatforms,
    WhyChooseUs,
    DevelopmentProcess,
    WhatWeDo
)

class OurMasterySerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = OurMastery
        fields = ["name","content","image_url"]

    def get_image_url(self, obj):
        return obj.image.url

class HeroSectionSerializers(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = ["id","title","content","image"]
    
    def to_representation(self,obj):
        instance = super(HeroSectionSerializers,self).to_representation(obj)
        instance['title'] = instance['title'].title()
        return instance

class NotableBlockchainPlatformsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotableBlockchainPlatforms
        fields = ['name','image','content']
    
class WhyChooseUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyChooseUs
        fields = ['service_name','icon','content']

class BlockchainDevelopmentProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevelopmentProcess
        fields = ["title","content"]

class WhatWeDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatWeDo
        fields = ['title','content','image']

    
    # def to_representation(self, obj):
    #     instance = super(WhatWeDoSerializer, self).to_representation(obj)
    #     return instance