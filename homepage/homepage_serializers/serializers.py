from rest_framework import serializers
from homepage.models import (
    OurMastery,
    HeroSection,
    NotableBlockchainPlatforms,
    WhyChooseUs,
    DevelopmentProcess
)

class OurMasterySerializer(serializers.ModelSerializer):
    class Meta:
        model = OurMastery
        fields = ["name","image","content"]

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