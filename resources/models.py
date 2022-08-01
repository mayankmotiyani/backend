from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

# Create your models here.

class Resource(models.Model):
    name = models.CharField(_("resourceName"),max_length=250,blank=True)
    image = models.ImageField(_("resourceImage"),upload_to='resources')
    slug = models.SlugField(_("resourceSlug"),max_length=250,blank=True,null=True)
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    class Meta:
        verbose_name_plural = "Resource"
    
    def __str__(self):
        return "{}".format(self.name)

    def save(self, *args, **kwargs):
        self.name = slugify(self.slug)
        super(Resource,self).save(*args, **kwargs)

