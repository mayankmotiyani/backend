from rest_framework import serializers
from resources.models import (
    Resource
)
class ResourceSerializer(serializers.ModelSerializer):
    resource_url = serializers.SerializerMethodField()
    class Meta:
        model = Resource
        fields = ['name','resource_url']
    
    def get_resource_url(self,obj):
        return obj.get_absolute_url()