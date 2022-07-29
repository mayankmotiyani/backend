from django.contrib import admin
from django.utils.html import format_html
from .models import (
    About,
    ContactAddress
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
    
admin.site.register(About, AboutAdmin)
admin.site.register(ContactAddress, ContactAddressAdmin )
    







