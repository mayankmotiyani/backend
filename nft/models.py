from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class HeadingAndSubheading(models.Model):
    subheading = models.CharField(_('homepageSubheading'), max_length=500)
    heading = models.TextField(_('homepageHeading'),null=True,blank=True)
    description = models.TextField(_('description'),default="")
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    def __str__(self):
        return "{}".format(self.subheading)
    
    class Meta:
        verbose_name_plural = "Heading & Subheading"

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

class NFTSection2(models.Model):
    nft = models.ForeignKey(NFT,on_delete=models.CASCADE)
    heading = models.CharField(_("nftSection2Heading"),max_length=500)
    title = models.TextField(_("nftSection2Title"),blank=True,null=True)
    content = RichTextUploadingField(_("nftSection2Content"))
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    def __str__(self):
        return "{}".format(self.nft)


class NFTUseCases(models.Model):
    nft = models.ForeignKey(NFT,on_delete=models.CASCADE)
    heading = models.ForeignKey(HeadingAndSubheading, on_delete=models.CASCADE,null=True)
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
    heading = models.ForeignKey(HeadingAndSubheading, on_delete=models.CASCADE,null=True)
    title = models.CharField(_("serviceTitle"),max_length=500)
    content = models.TextField(_("serviceContent"))
    icon = models.ImageField(_("serviceIcon"),upload_to="nft_use_cases")
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    class Meta:
        verbose_name_plural = "NFT Marketplace Development Service"

    def __str__(self):
        return "{}".format(self.title)


