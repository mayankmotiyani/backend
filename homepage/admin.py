from django.contrib import admin
from django.utils.html import format_html
from .models import (
    OurMastery,
    HeroSection,
    NotableBlockchainPlatforms,
)
# Register your models here.

class HeroSectionAdmin(admin.ModelAdmin):
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

    list_display  = ['title','image','display_content','admin_created_at','admin_updated_at']

   
class OurMasteryAdmin(admin.ModelAdmin):
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

    list_display  = ['name','image','display_content','admin_created_at','admin_updated_at']

class NotableBlockchainPlatformsAdmin(admin.ModelAdmin):
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

    list_display  = ['name','image','display_content','admin_created_at','admin_updated_at']

admin.site.register(OurMastery, OurMasteryAdmin)
admin.site.register(NotableBlockchainPlatforms, NotableBlockchainPlatformsAdmin)
admin.site.register(HeroSection, HeroSectionAdmin)