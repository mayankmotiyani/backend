from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Blockchain,
    BlockchainCategory,
    OurUnparalleledService,
    DummySection2,
    DummySection3,
    HeadingAndSubheading
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


class BlockchainCategoryAdmin(admin.ModelAdmin):
    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')

    list_display  = ['blockchain_category','admin_created_at','admin_updated_at']



class BlockchainAdmin(admin.ModelAdmin):
    exclude = ('blockchain_slug',)
    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')

    list_display = ['blockchainCategory','blockchain_name','blockchain_slug','admin_created_at','admin_updated_at']


class OurUnparalleledServiceAdmin(admin.ModelAdmin):
    exclude = ('blockchain_slug',)
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

    list_display = ['blockchain','subheading','title','admin_created_at','admin_updated_at']


class DummySection2Admin(admin.ModelAdmin):
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

    list_display = ['blockchain','subheading','title','admin_created_at','admin_updated_at']


class DummySection3Admin(admin.ModelAdmin):
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

    list_display = ['blockchain','subheading','title','admin_created_at','admin_updated_at']


admin.site.register(BlockchainCategory, BlockchainCategoryAdmin)
admin.site.register(OurUnparalleledService, OurUnparalleledServiceAdmin)
admin.site.register(Blockchain, BlockchainAdmin)
admin.site.register(DummySection2, DummySection2Admin)
admin.site.register(DummySection3, DummySection3Admin)

