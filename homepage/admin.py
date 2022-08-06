from django.contrib import admin
from django.utils.html import format_html
from .models import (
    OurMastery,
    HeroSection,
    WhyChooseUs,
    DevelopmentProcess,
    WhatWeDo,
    HeadingAndSubheading,
    StartSomethingUndeniably,
    BlogSection,
    TestimonialSection

)
# Register your models here.
class StartSomethingUndeniablyAdmin(admin.ModelAdmin):

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

    list_display  = ['subheading','heading','display_content','admin_created_at','admin_updated_at']


class BlogSectionAdmin(admin.ModelAdmin):

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

    list_display  = ['subheading','content','display_content','admin_created_at','admin_updated_at']

class TestimonialSectionAdmin(admin.ModelAdmin):

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

    list_display  = ['subheading','content','display_content','admin_created_at','admin_updated_at']

class HeadingAndSubheadingAdmin(admin.ModelAdmin):

    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')

    list_display  = ['subheading','heading','admin_created_at','admin_updated_at']

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

    # This will help you to disable add functionality
    def has_add_permission(self, request):
        get_our_mastery_instance = OurMastery.objects.all()
        if len(get_our_mastery_instance) >=6:
            return False
        return True

    # This will help you to disable delete functionality
    def has_delete_permission(self, request, obj=None):
        return False
        
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

# class NotableBlockchainPlatformsAdmin(admin.ModelAdmin):
#     @admin.display(description='CreationDate')
#     def admin_created_at(self, obj):
#         return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
#     @admin.display(description='UpdatedDate')
#     def admin_updated_at(self, obj):
#         return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')

#     @admin.display(description='content')
#     def display_content(self, obj):
#         return format_html(
#             '<textarea cols="60" rows="4" readonly>{}</textarea>',
#             obj.content)

#     list_display  = ['name','image','display_content','admin_created_at','admin_updated_at']


class WhyChooseUsAdmin(admin.ModelAdmin):
    
    # This will help you to disable add functionality
    def has_add_permission(self, request):
        get_why_choose_us_instance = WhyChooseUs.objects.all()
        if len(get_why_choose_us_instance) >=6:
            return False
        return True

    # This will help you to disable delete functionality
    def has_delete_permission(self, request, obj=None):
        return False

    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdateDate')
    def admin_updated_at(self,obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')
    
    list_display = ['service_name','admin_created_at','admin_updated_at']


class DevelopmentProcessAdmin(admin.ModelAdmin):

    # This will help you to disable add functionality
    def has_add_permission(self, request):
        return False

    # This will help you to disable delete functionality
    def has_delete_permission(self, request, obj=None):
        return False

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


class WhatWeDoAdmin(admin.ModelAdmin):

    # This will help you to disable add functionality
    def has_add_permission(self, request):
        get_what_we_do_instance = WhatWeDo.objects.all()
        if len(get_what_we_do_instance) >=2:
            return False
        return True

    # This will help you to disable delete functionality
    def has_delete_permission(self, request, obj=None):
        return False

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


admin.site.register(HeadingAndSubheading, HeadingAndSubheadingAdmin)
admin.site.register(OurMastery, OurMasteryAdmin)
# admin.site.register(NotableBlockchainPlatforms, NotableBlockchainPlatformsAdmin)
admin.site.register(HeroSection, HeroSectionAdmin)
admin.site.register(WhyChooseUs,WhyChooseUsAdmin)
admin.site.register(DevelopmentProcess, DevelopmentProcessAdmin)
admin.site.register(WhatWeDo, WhatWeDoAdmin)

admin.site.register(StartSomethingUndeniably,StartSomethingUndeniablyAdmin)
admin.site.register(BlogSection, BlogSectionAdmin)
admin.site.register(TestimonialSection, TestimonialSectionAdmin)