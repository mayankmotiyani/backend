import re
from dataclasses import field
from rest_framework import serializers
from django.utils.text import Truncator
from company.models import (
    Team,
    Careers,
    ApplyForJob
    
)

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['member_name','member_avatar','member_profile','member_bio']


class CareerSerializer(serializers.ModelSerializer):
    career_url = serializers.SerializerMethodField()
    class Meta:
        model = Careers
        fields = ['opening_designation','designation_brief','experience','location','opening','join_duration','career_url']
    
    def get_career_url(self,obj):
        return obj.get_absolute_url()
    
    def to_representation(self, obj):
        instance = super(CareerSerializer, self).to_representation(obj)
        instance['designation_brief'] = Truncator(instance['designation_brief']).words(20)
        return instance
 
class SingleCareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Careers
        fields = ['opening_designation','designation_brief','experience','location','opening','join_duration','skills','responsibilities']
    
    def to_representation(self, obj):
        instance = super(SingleCareerSerializer, self).to_representation(obj)
        instance['skills'] = re.sub('\\t*\\r*\\n*\\\\*', '', instance['skills'])
        instance['responsibilities'] = re.sub('\\t*\\r*\\n*\\\\*', '', instance['responsibilities'])
        return instance

class ApplyForJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplyForJob
        fields = "__all__"