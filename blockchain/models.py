from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField

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

class BlockchainCategory(models.Model):
    blockchain_category = models.CharField(_("blockchainCategory"), max_length=100)
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    class Meta:
        verbose_name_plural = "Blockchain Category"

    def __str__(self):
        return '{}'.format(self.blockchain_category)


class Blockchain(models.Model):
    blockchainCategory = models.ForeignKey(BlockchainCategory,on_delete=models.CASCADE)
    blockchain_name = models.CharField(_("blockchainName"),max_length=250,default="")
    blockchain_slug = models.SlugField(_("blockchainSlug"),max_length=250,blank=True,null=True,default="")
    blockchain_description = models.TextField(_("blockchainDescription"),blank=True,null=True)
    # blockchain_content = RichTextUploadingField(_("blockchainContent"),blank=True,null=True)
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    class Meta:
        verbose_name_plural = "Blockchain"

   
    def save(self, *args, **kwargs):
        self.blockchain_slug = slugify(self.blockchain_name)
        super(Blockchain, self).save(*args, **kwargs)


    def __str__(self):
        return '{} -- {}'.format(self.blockchainCategory.blockchain_category,self.blockchain_name)


    def get_absolute_url(self):
        return reverse('blockchain',kwargs={'blockchain_slug':self.blockchain_slug})


# class BlockchainService(models.Model):
#     blockchain = models.ForeignKey(Blockchain,on_delete=models.CASCADE)
#     blockchain_service_name = models.CharField(_("blockchainServiceName"),max_length=250)
#     blockchain_service_slug = models.SlugField(_("blockchainServiceSlug"),max_length=250,blank=True,null=True,default="")
#     blockchain_content = models.TextField(_("blockchainContent"),blank=True,null=True,default="")
#     created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
#     updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

#     class Meta:
#         verbose_name_plural = "Blockchain Service"

#     def save(self, *args, **kwargs):
#         self.blockchain_service_slug = slugify(self.blockchain_service_name)
#         super(BlockchainService, self).save(*args, **kwargs)
    
#     def __str__(self):
#         return '{} -- {}'.format(self.blockchain,self.blockchain_service_name)



# class WhatWeOffer(models.Model):
#     blockchain = models.ForeignKey(Blockchain,on_delete=models.CASCADE)
#     blockchain_name = models.CharField(_("blockchainName"), max_length=250)
#     icon = models.ImageField(_("icon"), upload_to="icon")
#     content = models.TextField(_("content"))
#     created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
#     updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)
    
#     def __str__(self) :
#         return self.blockchain_name

class OurUnparalleledService(models.Model):
    blockchain = models.ForeignKey(Blockchain,on_delete=models.CASCADE,null=True,blank=True)
    subheading = models.CharField(_("subHeading"),max_length=500,null=True,blank=True)
    title = models.CharField(_("UnparalleledServiceTitle"),max_length=500)
    content = models.TextField(_("UnparalleledServiceContent"))
    image = models.ImageField(upload_to="blockchain_section_1",null=True)
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    def __str__(self):
        return "{}".format(self.blockchain)
    
    class Meta:
        verbose_name_plural = "Blockchain Section 1"

class DummySection2(models.Model):
    blockchain = models.ForeignKey(Blockchain,on_delete=models.CASCADE,null=True,blank=True)
    subheading = models.CharField(_("subHeading"),max_length=500,null=True,blank=True)
    title = models.CharField(_("dummySectionTitle"),max_length=500)
    content = models.TextField(_("dummySectionContent"))
    image = models.ImageField(upload_to="blockchain_section_1",null=True)
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    def __str__(self):
        return "{}".format(self.title)
    
    class Meta:
        verbose_name_plural = "Blockchain Section 2"

class DummySection3(models.Model):
    blockchain = models.ForeignKey(Blockchain,on_delete=models.CASCADE,null=True,blank=True)
    subheading = models.CharField(_("subHeading"),max_length=500,null=True,blank=True)
    title = models.CharField(_("dummySectionTitle"),max_length=500)
    content = models.TextField(_("dummySectionContent"))
    image = models.ImageField(upload_to="blockchain_section_1",null=True)
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    def __str__(self):
        return "{}".format(self.title)
    
    class Meta:
        verbose_name_plural = "Blockchain Section 3"



