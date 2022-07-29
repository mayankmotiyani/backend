from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

# Create your models here.

class About(models.Model):
    name = models.CharField(_("name"), max_length=100)
    image = models.ImageField(_("image"),upload_to="about")
    slug = models.SlugField(_("aboutSlug"), max_length=100, blank=True)
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(About, self).save(*args, **kwargs)
       
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "About"
    
class ContactAddress(models.Model):
    office = models.CharField(_("officeName"),max_length=250,unique=True)
    location = models.TextField(_("officeLocation"))
    phone = models.CharField(_("officeNumbers"),max_length=500,help_text="use , seperator for officeNumber",blank=True,null=True,default="")
    email = models.CharField(_("officeEmails"),max_length=500,help_text="use , seperator for officeEmails",blank=True,null=True,default="")
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    def __str__(self):
        return "{}".format(self.office)

    class Meta:
        verbose_name_plural = "Contact Address"


    


