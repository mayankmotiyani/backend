from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class OurMastery(models.Model):
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

class NotableBlockchainPlatforms(models.Model):
    name = models.CharField(_("name"),max_length=250)
    image = models.ImageField(_("image"),upload_to='notable_blockchain_platforms')
    content = models.TextField(_("content"))
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)


    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name_plural = "High-End Expertise In Blockchain"
        

class WhyChooseUs(models.Model):
    service_name = models.CharField(_("chooseServiceName"), max_length=250)
    icon = models.ImageField(_("icon"), upload_to="why_choose_us")
    content = models.TextField(_("content"))
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    class Meta:
        verbose_name_plural = "Why Choose Us"
        
    def __str__(self) :
        return self.service_name

class DevelopmentProcess(models.Model):
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
    title = models.CharField(_("whatWeDoTitle"),max_length=500)
    content = models.TextField(_("whatWeDoContent"))
    image = models.ImageField(_("whatWeDoImage"),upload_to="what_we_do")
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    class Meta:
        verbose_name_plural = "What We Do"
    
    def __str__(self):
        return "{}".format(self.title)