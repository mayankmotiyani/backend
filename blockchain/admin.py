from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Blockchain,
    BlockchainCategory,
    BlockchainService,
)
# Register your models here.

class BlockchainCategoryAdmin(admin.ModelAdmin):
    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')

    list_display  = ['blockchain_category','admin_created_at','admin_updated_at']



class BlockchainAdmin(admin.ModelAdmin):
    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')

    list_display = ['blockchainCategory','blockchain_name','blockchain_slug','admin_created_at','admin_updated_at']


class BlockchainServiceAdmin(admin.ModelAdmin):
    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')

    @admin.display(description='content')
    def display_blockchain_content(self, obj):
        return format_html(
            '<textarea cols="60" rows="4" readonly>{}</textarea>',
            obj.blockchain_content)

    list_display = ['blockchain','blockchain_service_name','blockchain_service_slug','display_blockchain_content','admin_created_at','admin_updated_at']


admin.site.register(BlockchainCategory, BlockchainCategoryAdmin)
admin.site.register(BlockchainService, BlockchainServiceAdmin)
admin.site.register(Blockchain, BlockchainAdmin)
