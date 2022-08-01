from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Organization,
    Product
)
# Register your models here.

class OrganizationAdmin(admin.ModelAdmin):
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

class ProductAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')

    list_display  = ['organization','name','admin_created_at','admin_updated_at']

admin.site.register(Organization,OrganizationAdmin)
admin.site.register(Product,ProductAdmin)