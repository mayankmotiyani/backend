import re
from dataclasses import field
from rest_framework import serializers
from about_company.models import (
    ContactAddress,
    PrivacyPolicy,
    TermsAndCondition,
    AboutCompany,
    HeadingAndSubheading,
    AboutCompanySection1

)

class HeadingAndSubheadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeadingAndSubheading
        fields = ['subheading','heading']
    
    def to_representation(self, obj):
        instance = super(HeadingAndSubheadingSerializer,self).to_representation(obj)
        if instance['heading'] == "":
            del instance['heading']
        return instance

class AboutCompanySection1Serializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCompanySection1
        fields = "__all__"

class AboutCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCompany
        fields = ['description']


class OfficeAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactAddress
        fields = ['id','office','location','phone','email']

    def to_representation(self,obj):
        instance = super(OfficeAddressSerializer,self).to_representation(obj)
        print(instance)
        if instance['email'] == None:
            instance['email'] = ""
        else:
            instance['email'] = instance['email'].replace(",","|")
        instance['phone'] = instance['phone'].replace(",","|")
        return instance
            
class HeaderOfficeAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactAddress
        fields = ['office','phone']
    
class PrivacyPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicy
        fields = ['title','description','content']
    
    def to_representation(self, obj):
        instance = super(PrivacyPolicySerializer, self).to_representation(obj)
        instance['content'] = re.sub('\\t*\\r*\\n*\\\\*', '', instance['content'])
        return instance


class TermsAndConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermsAndCondition
        fields = ['title','description','content']
    
    def to_representation(self, obj):
        instance = super(TermsAndConditionSerializer, self).to_representation(obj)
        instance['content'] = re.sub('\\t*\\r*\\n*\\\\*', '', instance['content'])
        return instance