from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Portfolio(models.Model):
    name = models.CharField(_("portfolioName"),max_length=250)
    image = models.ImageField(_("portfolioImage"),upload_to="portfolio_images")
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    class Meta:
        verbose_name_plural = "Portfolio"

    def __str__(self):
        return "{}".format(self.name)


class CaseStudy(models.Model):
    pass