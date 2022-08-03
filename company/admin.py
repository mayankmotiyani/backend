from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Team,
    Testimonial,
    Help,
    Careers,
    ApplyForJob
)

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='content')
    def display_member_bio(self, obj):
        return format_html(
            '<textarea cols="60" rows="4" readonly>{}</textarea>',
            obj.member_bio)

    list_display  = ['member_unique_id','member_name','member_avatar','member_profile','display_member_bio','admin_created_at','admin_updated_at']


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


class HelpAdmin(admin.ModelAdmin):
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

    list_display  = ['topic','display_content','admin_created_at','admin_updated_at']


class CareerAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='content')
    def display_designation_brief(self, obj):
        return format_html(
            '<textarea cols="60" rows="4" readonly>{}</textarea>',
            obj.designation_brief)

    list_display  = ['opening_designation','display_designation_brief','opening','experience','location','admin_created_at','admin_updated_at','opening_available']


class ApplyForJobAdmin(admin.ModelAdmin):
    @admin.display(description='CreationDate')
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %I:%M %p')
    
    @admin.display(description='UpdatedDate')
    def admin_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%d %I:%M %p')
    
    list_display = ['name','email','contact','skill_set','admin_created_at','admin_updated_at']

admin.site.register(Team, TeamAdmin)
admin.site.register(Testimonial,TestimonialAdmin)
admin.site.register(Help,HelpAdmin)
admin.site.register(Careers,CareerAdmin)
admin.site.register(ApplyForJob,ApplyForJobAdmin)



