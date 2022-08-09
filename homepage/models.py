from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify
from django.urls import reverse 
from product.models import (
    Product,
)

# Create your models here.

class HeadingAndSubheading(models.Model):
    subheading = models.CharField(_('homepageSubheading'), max_length=500,default="")
    heading = models.TextField(_('homepageHeading'),null=True,blank=True,default="")
    description = models.TextField(_('description'),default="")
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)


    def __str__(self):
        return "{}".format(self.subheading)
    
    class Meta:
        verbose_name_plural = "Heading & Subheading"


class ProfessionalBlockchainDevelopmentCompany(models.Model):
    heading_and_subheading = models.ForeignKey(HeadingAndSubheading,on_delete=models.CASCADE,null=True)
    name = models.CharField(_("nichesName"),max_length=250)
    image = models.ImageField(_("nicheImages"),upload_to='niche_images')
    content = models.TextField(_("nicheContent"))
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    class Meta:
        verbose_name_plural = "Professional Blockchain Development Company"

    def __str__(self):
        return "{}".format(self.name)

class Banner(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    title = models.CharField(_("title"),max_length=500)
    content = models.TextField(_("content"))
    image = models.ImageField(_("image"),upload_to='hero_section_images')
    official_link = models.URLField(_("official_link"),null=True,blank=True,max_length=500)
    slug = models.SlugField(_("slug"),max_length=200,null=True,blank=True)
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product.name)
        super(HeroSection, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Banner"
    
    def __str__(self):
        return "{}".format(self.title)

    def get_absolute_url(self):
        return reverse('product',kwargs={'product_url':self.slug})
       

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
    heading = models.CharField(_("whatWeDoHeading"),max_length=250,null=True,blank=True,default="")
    title = models.CharField(_("whatWeDoTitle"),max_length=500)
    content = models.TextField(_("whatWeDoContent"))
    image = models.ImageField(_("whatWeDoImage"),upload_to="what_we_do")
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    class Meta:
        verbose_name_plural = "What We Do"
    
    def __str__(self):
        return "{}".format(self.title)

class BlockchainTechnology(models.Model):
    subheading = models.CharField(_("subHeading"),max_length=500,null=True,blank=True,default="")
    heading = models.CharField(_("heading"),max_length=500)
    content = models.TextField(_("content"))
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    def __str__(self):
        return "{}".format(self.subheading)

    class Meta:
        verbose_name_plural = "Blockchain Technology"

class BlogSection(models.Model):
    subheading = models.CharField(_("blogSubheading"),max_length=500,null=True,blank=True,default="")
    content = models.TextField(_("blogContent"))
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    def __str__(self):
        return "{}".format(self.subheading)

    class Meta:
        verbose_name_plural = "Our Blogs"


class TestimonialSection(models.Model):
    subheading = models.CharField(_("testimonialSubheading"),max_length=500,default="")
    content = models.TextField(_("testimonialsContent"))
    image = models.ImageField(_("clientImage"),null=True,upload_to="testimonials")
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    def __str__(self):
        return "{}".format(self.subheading)
    
    class Meta:
        verbose_name_plural = "Testimonial Section"

class Partner(models.Model):
    image = models.ImageField(_("partnerImage"),upload_to="partner_images")
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    def __str__(self):
        return "Partners"
    
    class Meta:
        verbose_name_plural = "Our Partners"

class GetInTouch(models.Model):
    heading = models.CharField(_("heading"),max_length=100)
    description = models.TextField(_("description"))
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    def __str__(self):
        return "Get In Touch"
    
    class Meta:
        verbose_name_plural = "Get In Touch"




class ContactInformation(models.Model):
    description = models.TextField(_("description"))
    email = models.EmailField(_("email"))
    phone = models.CharField(_("phone"),max_length=100)
    on_the_web = models.EmailField(_("on-the-web"))
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)


    def __str__(self):
        return "{}".format(self.email)

    class Meta:
        verbose_name_plural = "Contact Information"

class Testimonial(models.Model):
    client_name = models.CharField(_("clientName"),max_length=250,default="")
    client_feedback = models.TextField(_("clientFeedback"),default="")
    image = models.ImageField(_("clientImage"),null=True,upload_to="testimonials")
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Testimonial"
    
    def __str__(self):
        return "{}".format(self.client_name)
