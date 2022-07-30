from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class NFT(models.Model):
    name = models.CharField(_("NftName"),max_length=250)
    slug = models.SlugField(_("NftSlug"),max_length=250,blank=True,null=True)
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)
    
    class Meta:
        verbose_name_plural = "NFT"

    def __str__(self):
        return "{}".format(self.name)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(NFT, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("nft",kwargs={'nft_slug':self.slug})
    