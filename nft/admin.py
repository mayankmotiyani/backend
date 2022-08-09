from django.contrib import admin
from django.utils.html import format_html
from .models import (
    NFT,
    NFTUseCases,
    NFTMarketplaceDevelopmentService,
    NFTSection2,
    HeadingAndSubheading,
    
)

# Register your models here.
class HeadingAndSubheadingAdmin(admin.ModelAdmin):
    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')

    list_display  = ['subheading','heading','description','admin_created_at','admin_updated_at']


class NFTSection2Admin(admin.ModelAdmin):
    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='title')
    def display_title(self, obj):
        return format_html(
            '<textarea cols="60" rows="4" readonly>{}</textarea>',
            obj.title)

    list_display  = ['nft','heading','display_title','admin_created_at','admin_updated_at']


class NFTAdmin(admin.ModelAdmin):
    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='description')
    def display_description(self, obj):
        return format_html(
            '<textarea cols="60" rows="4" readonly>{}</textarea>',
            obj.description)

    list_display  = ['name','display_description','admin_created_at','admin_updated_at']

class NFTUseCasesAdmin(admin.ModelAdmin):
    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='content')
    def display_content(self, obj):
        return format_html(
            '<textarea cols="60" rows="4" readonly>{}</textarea>',
            obj.content)

    list_display  = ['nft','heading','title','display_content','admin_created_at','admin_updated_at']

class NFTMarketplaceDevelopmentServiceAdmin(admin.ModelAdmin):
    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='content')
    def display_content(self, obj):
        return format_html(
            '<textarea cols="60" rows="4" readonly>{}</textarea>',
            obj.content)

    list_display  = ['nft','heading','title','display_content','admin_created_at','admin_updated_at']

admin.site.register(NFT, NFTAdmin)
admin.site.register(NFTSection2, NFTSection2Admin)
admin.site.register(HeadingAndSubheading, HeadingAndSubheadingAdmin)
admin.site.register(NFTUseCases, NFTUseCasesAdmin)
admin.site.register(NFTMarketplaceDevelopmentService, NFTMarketplaceDevelopmentServiceAdmin)
