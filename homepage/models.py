from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
# Create your models here.


class HeadingAndSubheading(models.Model):
    subheading = models.CharField(_('homepageSubheading'), max_length=500)
    heading = models.TextField(_('homepageHeading'),null=True,blank=True)
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)


    def __str__(self):
        return "{}".format(self.subheading)
    
    class Meta:
        verbose_name_plural = "Heading & Subheading"


class OurMastery(models.Model):
    heading_and_subheading = models.ForeignKey(HeadingAndSubheading,on_delete=models.CASCADE,null=True)
    name = models.CharField(_("nichesName"),max_length=250)
    image = models.ImageField(_("nicheImages"),upload_to='niche_images')
    content = models.TextField(_("nicheContent"))
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    class Meta:
        verbose_name_plural = "Our Mastery"

    def __str__(self):
        return "{}".format(self.name)

class HeroSection(models.Model):
    title = models.CharField(_("title"),max_length=500)
    content = models.TextField(_("content"))
    image = models.ImageField(_("image"),upload_to='hero_section_images')
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    class Meta:
        verbose_name_plural = "Hero Section"
    
    def __str__(self):
        return "{}".format(self.title)
       

class WhyChooseUs(models.Model):
    heading_and_subheading = models.ForeignKey(HeadingAndSubheading,on_delete=models.CASCADE,null=True)
    service_name = models.CharField(_("chooseServiceName"), max_length=250)
    icon = models.FileField(_("icon"), upload_to="why_choose_us",validators=[FileExtensionValidator(['pdf', 'doc', 'svg'])])
    content = models.TextField(_("content"))
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    class Meta:
        verbose_name_plural = "Why Choose Us"
        
    def __str__(self) :
        return self.service_name

class DevelopmentProcess(models.Model):
    heading_and_subheading = models.ForeignKey(HeadingAndSubheading,on_delete=models.CASCADE,null=True)
    title = models.CharField(_("blockchainProcessTitle"),max_length=500)
    content = models.TextField(_("blockchainProcessContent"))
    image = models.ImageField(_("blockchainProcessImage"),upload_to="blockchain_process")
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    class Meta:
        verbose_name_plural = "Blockchain Development Process"
    
    def __str__(self):
        return "{}".format(self.title)

class WhatWeDo(models.Model):
    heading = models.CharField(_("whatWeDoHeading"),max_length=250,null=True)
    title = models.CharField(_("whatWeDoTitle"),max_length=500)
    content = models.TextField(_("whatWeDoContent"))
    image = models.ImageField(_("whatWeDoImage"),upload_to="what_we_do")
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    class Meta:
        verbose_name_plural = "What We Do"
    
    def __str__(self):
        return "{}".format(self.title)

class StartSomethingUndeniably(models.Model):
    subheading = models.CharField(_("subHeading"),max_length=500)
    heading = models.CharField(_("heading"),max_length=500)
    content = models.TextField(_("content"))
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    def __str__(self):
        return "{}".format(self.subheading)

class BlogSection(models.Model):
    subheading = models.CharField(_("blogSubheading"),max_length=500)
    content = models.TextField(_("blogContent"))
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    def __str__(self):
        return "{}".format(self.subheading)

class TestimonialSection(models.Model):
    subheading = models.CharField(_("testimonialSubheading"),max_length=500)
    content = models.TextField(_("testimonialsContent"))
    image = models.ImageField(_("clientImage"),null=True,upload_to="testimonials")
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    def __str__(self):
        return "{}".format(self.subheading)

class Partner(models.Model):
    image = models.ImageField(_("partnerImage"),upload_to="partner_images")
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    def __str__(self):
        return "Partners"
    
    class Meta:
        verbose_name_plural = "Partner"
