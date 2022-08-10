from django.contrib import admin
from django.utils.html import format_html
from .models import (
    ContactAddress,
    BecomeOurPartner,
    PrivacyPolicy,
    TermsAndCondition,
    HeadingAndSubheading,
    AboutCompany,
    UnmatchedServices,
    BlockchainForBusiness,
    VisionAndMission,
    Partners,
    FAQs

)

# Register your models here.

class HeadingAndSubheadingAdmin(admin.ModelAdmin):
    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')
    
    list_display  = ['subheading','heading','admin_created_at','admin_updated_at']


class AboutCompanyAdmin(admin.ModelAdmin):
    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')
    
    list_display  = ['heading','description','admin_created_at','admin_updated_at']


class UnmatchedServicesAdmin(admin.ModelAdmin):
    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')
    
    list_display  = ['heading','description','admin_created_at','admin_updated_at']


class BlockchainForBusinessAdmin(admin.ModelAdmin):
    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')
    
    list_display  = ['heading','image','title','description','admin_created_at','admin_updated_at']


class ContactAddressAdmin(admin.ModelAdmin):
    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')
    
    list_display  = ['office','location','phone','email','admin_created_at','admin_updated_at']


class BecomeOurPartnerAdmin(admin.ModelAdmin):

    @admin.display(description='fullName')
    def admin_full_name(self, obj):
        return obj.first_name + " " + obj.last_name

    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')
    
    list_display  = ['admin_full_name','email','contact','address','state','city','source','source_optional','notes','admin_created_at','admin_updated_at']



class PrivacyPolicyAdmin(admin.ModelAdmin):
    # This will help you to disable add functionality
    def has_add_permission(self, request):
        get_privacy_policy_instance = PrivacyPolicy.objects.all()
        if len(get_privacy_policy_instance) >=1:
            return False
        return True
    
    def has_delete_permission(self, request,obj=None):
        return False


class TermsAndConditionAdmin(admin.ModelAdmin):
    # This will help you to disable add functionality
    def has_add_permission(self, request):
        get_terms_and_condition_instance = TermsAndCondition.objects.all()
        if len(get_terms_and_condition_instance) >=1:
            return False
        return True
    
    def has_delete_permission(self, request,obj=None):
        return False


class VisionAndMissionAdmin(admin.ModelAdmin):

    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')
    
    list_display  = ['heading','image','admin_created_at','admin_updated_at']


class PartnersAdmin(admin.ModelAdmin):

    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')
    
    list_display  = ['heading','image','admin_created_at','admin_updated_at']

class FAQsAdmin(admin.ModelAdmin):
    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')
        
    list_display  = ['title','question','answer','admin_created_at','admin_updated_at']


admin.site.register(ContactAddress, ContactAddressAdmin)
admin.site.register(BecomeOurPartner, BecomeOurPartnerAdmin)
admin.site.register(PrivacyPolicy,PrivacyPolicyAdmin) 
admin.site.register(TermsAndCondition,TermsAndConditionAdmin)   
admin.site.register(HeadingAndSubheading,HeadingAndSubheadingAdmin) 
admin.site.register(AboutCompany,AboutCompanyAdmin)
admin.site.register(UnmatchedServices,UnmatchedServicesAdmin)    
admin.site.register(BlockchainForBusiness,BlockchainForBusinessAdmin)
admin.site.register(VisionAndMission,VisionAndMissionAdmin)    
admin.site.register(Partners,PartnersAdmin)
admin.site.register(FAQs,FAQsAdmin)






