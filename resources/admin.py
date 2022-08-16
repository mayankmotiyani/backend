from django.contrib import admin
from .models import (
    Resource
)

# Register your models here.

class ResourceAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')

    list_display  = ['name','image','admin_created_at','admin_updated_at']

admin.site.register(Resource,ResourceAdmin) 