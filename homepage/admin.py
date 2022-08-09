from django.contrib import admin
from django.utils.html import format_html
from django.conf import settings
from .models import (
    ProfessionalBlockchainDevelopmentCompany,
    Banner,
    WhyChooseUs,
    DevelopmentProcess,
    WhatWeDo,
    HeadingAndSubheading,
    BlockchainTechnology,
    BlogSection,
    TestimonialSection,
    Partner,
    GetInTouch,
    ContactInformation,
    Testimonial
)

# Register your models here.
def get_app_list(self, request):
    app_dict = self._build_app_dict(request)
    for app_name, object_list in app_dict.items():
        if app_name in settings.ADMIN_ORDERING:
            app = app_dict[app_name]
            app["models"].sort(
                key=lambda x: settings.ADMIN_ORDERING[app_name].index(x["object_name"])
            )
            app_dict[app_name]
            yield app
        else:
            yield app_dict[app_name]

class TestimonialAdmin(admin.ModelAdmin):
    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='content')
    def display_client_feedback(self, obj):
        return format_html(
            '<textarea cols="60" rows="4" readonly>{}</textarea>',
            obj.client_feedback)

    list_display  = ['client_name','display_client_feedback','admin_created_at','admin_updated_at']


class ContactInformationAdmin(admin.ModelAdmin):

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
    
    list_display  = ['email','phone','display_description','on_the_web','admin_created_at','admin_updated_at']



class GetInTouchAdmin(admin.ModelAdmin):

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
    
    list_display  = ['heading','display_description','admin_created_at','admin_updated_at']

class PartnerAdmin(admin.ModelAdmin):
    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')
    
    list_display  = ['id','image','admin_created_at','admin_updated_at']

class BlockchainTechnologyAdmin(admin.ModelAdmin):

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

    list_display  = ['subheading','content','image','display_content','admin_created_at','admin_updated_at']

class HeadingAndSubheadingAdmin(admin.ModelAdmin):

    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')

    list_display  = ['subheading','heading','admin_created_at','admin_updated_at']

class BannerAdmin(admin.ModelAdmin):

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

   
class ProfessionalBlockchainDevelopmentCompanyAdmin(admin.ModelAdmin):

    # This will help you to disable add functionality
    def has_add_permission(self, request):
        get_our_mastery_instance = ProfessionalBlockchainDevelopmentCompany.objects.all()
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
admin.site.register(ProfessionalBlockchainDevelopmentCompany, ProfessionalBlockchainDevelopmentCompanyAdmin)
# admin.site.register(NotableBlockchainPlatforms, NotableBlockchainPlatformsAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(WhyChooseUs,WhyChooseUsAdmin)
admin.site.register(DevelopmentProcess, DevelopmentProcessAdmin)
admin.site.register(WhatWeDo, WhatWeDoAdmin)

admin.site.register(BlockchainTechnology,BlockchainTechnologyAdmin)
admin.site.register(BlogSection, BlogSectionAdmin)
admin.site.register(TestimonialSection, TestimonialSectionAdmin)
admin.site.register(Partner,PartnerAdmin)
admin.site.register(GetInTouch,GetInTouchAdmin)
admin.site.register(ContactInformation,ContactInformationAdmin)
admin.site.register(Testimonial,TestimonialAdmin)

admin.AdminSite.get_app_list = get_app_list