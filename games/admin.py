from django.contrib import admin
from .models import (
    Game,
    ModernSolutionForVariousPlatform,
    GameSection2,
    GameSection3,
    HeadingAndSubheading,
    GamePartner
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



class GameAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    
    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')

    list_display  = ['name','description','admin_created_at','admin_updated_at']

class ModernSolutionForVariousPlatformAdmin(admin.ModelAdmin):
    
    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')

    list_display  = ['game','subheading','title','content','admin_created_at','admin_updated_at']

class GameSection2Admin(admin.ModelAdmin):
    
    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')

    list_display  = ['game','title','content','admin_created_at','admin_updated_at']

class GameSection3Admin(admin.ModelAdmin):
    
    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')

    list_display  = ['game','title','content','admin_created_at','admin_updated_at']


class GamePartnerAdmin(admin.ModelAdmin):
    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')

    list_display  = ['heading','image','admin_created_at','admin_updated_at']


admin.site.register(Game, GameAdmin) 
admin.site.register(ModernSolutionForVariousPlatform, ModernSolutionForVariousPlatformAdmin)
admin.site.register(GameSection2, GameSection2Admin)
admin.site.register(GameSection3, GameSection3Admin)
admin.site.register(HeadingAndSubheading,HeadingAndSubheadingAdmin)
admin.site.register(GamePartner,GamePartnerAdmin)