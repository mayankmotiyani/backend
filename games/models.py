from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class GameCategory(models.Model):
    name = models.CharField(_("gameName"),max_length=250)
    slug = models.SlugField(_("slug"),max_length=250,blank=True,null=True)
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    class Meta:
        verbose_name_plural = "Game Category"

    def __str__(self):
        return "{}".format(self.name)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(GameCategory,self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("game",kwargs={"game_slug":self.slug})

class Game(models.Model):
    pass


    

    



    

    
   