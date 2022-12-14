from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class HeadingAndSubheading(models.Model):
    subheading = models.CharField(_('homepageSubheading'), max_length=500,null=True,blank=True)
    heading = models.TextField(_('homepageHeading'),null=True,blank=True)
    description = models.TextField(_('description'),default="",null=True,blank=True)
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    def __str__(self):
        return "{}".format(self.subheading)
    
    class Meta:
        verbose_name_plural = "Heading & Subheading"

        
class Game(models.Model):
    name = models.CharField(_("gameName"),max_length=250)
    slug = models.SlugField(_("slug"),max_length=250,blank=True,null=True)
    description = models.TextField(_("gameDescription"),blank=True,null=True)
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    class Meta:
        verbose_name_plural = "Game"

    def __str__(self):
        return "{}".format(self.name)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Game,self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("game",kwargs={"game_slug":self.slug})


class ModernSolutionForVariousPlatform(models.Model):
    game = models.ForeignKey(Game,on_delete=models.CASCADE)
    subheading = models.CharField(_("modernSolutionSubHeading"),max_length=500, default= "")
    title = models.CharField(_("modernSolutionGameTitle"),max_length=500)
    content = models.TextField(_("modernSolutionGameContent"))
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    class Meta:
        verbose_name_plural = "Modern Solution For Various Platform"
    
    def __str__(self):
        return "{}".format(self.title.upper())


class GameSection2(models.Model):
    game = models.ForeignKey(Game,on_delete=models.CASCADE)
    heading = models.ForeignKey(HeadingAndSubheading,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(_("GameTitle"),max_length=500)
    image = models.ImageField(_("image"),upload_to="game")
    content = models.TextField(_("GameContent"))
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    def __str__(self):
        return "{}".format(self.title)
    

class GameSection3(models.Model):
    game = models.ForeignKey(Game,on_delete=models.CASCADE)
    title = models.CharField(_("GameTitle"),max_length=500)
    image = models.ImageField(_("image"),upload_to="game")
    content = models.TextField(_("GameContent"))
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    def __str__(self):
        return "{}".format(self.title) 


class GamePartner(models.Model):
    heading = models.ForeignKey(HeadingAndSubheading,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="game_partners")
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)


    class Meta:
        verbose_name_plural = "Game Partners"