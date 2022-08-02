import re
from dataclasses import field
from rest_framework import serializers
from company.models import (
    Team,
    Testimonial,
    Careers,
   
    
)

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['member_name','member_avatar','member_profile','member_bio']

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['client_name','client_feedback']

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Careers
        fields = '__all__'
    
    def to_representation(self, obj):
        instance = super(CareerSerializer, self).to_representation(obj)
        instance['skills'] = re.sub('\\t*\\r*\\n*\\\\*', '', instance['skills'])
        instance['responsibilities'] = re.sub('\\t*\\r*\\n*\\\\*', '', instance['responsibilities'])
        return instance
 
        
        