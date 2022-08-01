from django.contrib import admin
from django.utils.html import format_html
from .models import (
    About,
    ContactAddress,
    BecomeOurPartner
)
# Register your models here.


class AboutAdmin(admin.ModelAdmin):
    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')
    
    list_display  = ['name','image','admin_created_at','admin_updated_at']


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

    # @admin.display(description='address')
    # def display_member_bio(self, obj):
    #     return format_html(
    #         '<textarea cols="60" rows="4" readonly>{}</textarea>',
    #         obj.member_bio)
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')
    
    list_display  = ['admin_full_name','email','contact','address','state','city','source','source_optional','notes','admin_created_at','admin_updated_at']
    
admin.site.register(About, AboutAdmin)
admin.site.register(ContactAddress, ContactAddressAdmin )
admin.site.register(BecomeOurPartner, BecomeOurPartnerAdmin )
    







