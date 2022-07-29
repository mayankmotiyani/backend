import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField



# Create your models here.
class Team(models.Model):
    member_unique_id = models.IntegerField(_("memberID"),unique=True)
    member_name = models.CharField(_("memberName"),max_length=250)
    member_avatar = models.ImageField(_("memberAvatar"),upload_to='team_avatar')
    member_profile = models.CharField(_("memberDesignation"),max_length=250)
    member_bio = models.TextField(_("memberBio"))
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True) 

    def save(self, *args, **kwargs):
        self.member_name = self.member_name.title()
        super(Team,self).save(*args,**kwargs)

    class Meta:
        ordering = ["member_unique_id"]
        verbose_name_plural = "Team Members"

    def __str__(self):
        return "{}".format(self.member_name)


class Careers(models.Model):
    opening_designation = models.CharField(_("openingDesignation"),max_length=500,null=True)
    # designation_Image = models.ImageField(_("designationImage"),upload_to='designation_images')
    designation_brief = models.TextField(_("designationBrief"),null=True)
    experience = models.CharField(_("experience"),max_length=250,null=True,help_text="for example : 6 Months - 1 Year")
    location = models.CharField(_("location"),max_length=250,null=True)
    skills = RichTextUploadingField(_("careerSkills"),blank=True,null=True)
    responsibilities = RichTextUploadingField(_("careerResponsibilities"),blank=True,null=True)
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)


    class Meta:
        verbose_name_plural = "Career"

    def __str__(self):
        return '{}'.format(self.opening_designation)



class Testimonial(models.Model):
    client_name = models.CharField(_("clientName"),max_length=250,default="")
    client_feedback = models.TextField(_("clientFeedback"),default="")
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Testimonials"
    
    def __str__(self):
        return "{}".format(self.client_name)

    
class SiteMap(models.Model):
    pass

class PrivacyPolicy(models.Model):
    pass

class Event(models.Model):
    pass


class Help(models.Model):
    topic = models.CharField(_("topic"),max_length=250)
    content = models.TextField(_("content"))
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    class Meta:
        ordering = ['id']
        verbose_name_plural = "How Can We Help!"

