from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse 
# Create your models here.



class Organization(models.Model):
    name = models.CharField(_("organizationName"),max_length=500)
    content = models.TextField(_("content"))
    image = models.ImageField(_("organizationImage"),upload_to="organization")
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    class Meta:
        verbose_name_plural = "Organization"
    
    def __str__(self):
        return "{}".format(self.name)


class Product(models.Model):
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE)
    name = models.CharField(_("productName"),max_length=500)
    slug = models.SlugField(_("slug"),max_length=500,blank=True,null=True)
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    class Meta:
        verbose_name_plural = "Product"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)
    
    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        return reverse("product",kwargs={'product_url':self.slug})


class Product_goal(models.Model):
    title = models.CharField(_("tiitle"), max_length=250)
    subheading = models.CharField(_("subHeading"),max_length=250)
    content = models.TextField(_("content"))
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)
    
    def __str__(self):
        return '{}'.format(self.title)
    
class Product_method(models.Model):
    title = models.CharField(_("title"),max_length=250)
    subheading = models.CharField(_("subHeading"), max_length=250)
    content = models.TextFiled(_("content"))
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)
    
    def __str__(self):
        return '{}'.format(self.title)

class Product_functionality(models.Model):
    title = models.CharField(_("title"),max_length=250)
    subheading = models.CharField(_("subHeading"),max_length=250)
    content = models.TextField(_("content"))
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)
    
    def __str__(self):
        return '{}'.format(self.title)

class Conclusion_section(models.Model):
    title = models.CharField(_("title"),max_length=250)
    content = models.TextField(_("content"))
    image = models.ImageField(_("image"), upload_to="productImages")
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)
    
    def __str__(self):
        return '{}'.format(self.title)

