from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Game(models.Model):
    name = models.CharField(_("gameName"),max_length=250)
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    class Meta:
        verbose_name_plural = "Game"

    def __str__(self):
        return "{}".format(self.name)
    
   