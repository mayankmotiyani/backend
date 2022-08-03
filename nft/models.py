from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class NFT(models.Model):
    name = models.CharField(_("NftName"),max_length=250)
    description = models.TextField(_("NftDescription"),blank=True,null=True)
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
    

class NFTUseCases(models.Model):
    nft = models.ForeignKey(NFT,on_delete=models.CASCADE)
    title = models.CharField(_("useCasesTitle"),max_length=500)
    content = models.TextField(_("useCasesContent"))
    icon = models.ImageField(_("useCasesIcon"),upload_to="nft_use_cases")
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    class Meta:
        verbose_name_plural = "NFT Use Cases"

    def __str__(self):
        return "{}".format(self.title)


class NFTMarketplaceDevelopmentService(models.Model):
    nft = models.ForeignKey(NFT,on_delete=models.CASCADE)
    title = models.CharField(_("serviceTitle"),max_length=500)
    content = models.TextField(_("serviceContent"))
    icon = models.ImageField(_("serviceIcon"),upload_to="nft_use_cases")
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    class Meta:
        verbose_name_plural = "NFT Marketplace Development Service"

    def __str__(self):
        return "{}".format(self.title)

