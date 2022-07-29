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
 
        
        