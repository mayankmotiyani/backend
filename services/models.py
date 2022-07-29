from email.mime import image
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(_("servicesSlug"),max_length=100,blank=True )
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Service, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Service"
        
    def __str__(self):
        return self.name
    
class Content(models.Model):
    pass
   