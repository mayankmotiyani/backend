from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Portfolio
)

# Register your models here.
class PortfolioAdmin(admin.ModelAdmin):
    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')
    
    def image_tag(self, instance):
        return format_html('<img src="{}" />'.format(instance.image.url))

    list_display  = ['name','image','admin_created_at','admin_updated_at']

admin.site.register(Portfolio, PortfolioAdmin)