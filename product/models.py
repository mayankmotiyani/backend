from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse 
# Create your models here.

class HeadingAndSubheading(models.Model):
    subheading = models.CharField(_('homepageSubheading'), max_length=500)
    heading = models.TextField(_('homepageHeading'),null=True,blank=True)
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    def __str__(self):
        return "{}".format(self.subheading)
    
    class Meta:
        verbose_name_plural = "Heading & Subheading"

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


class OurGoal(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    heading = models.ForeignKey(HeadingAndSubheading, on_delete=models.CASCADE,null=True)
    title = models.CharField(_("productGoalTitle"), max_length=250)
    content = models.TextField(_("productGoalContent"))
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)
    
    def __str__(self):
        return '{}'.format(self.title)
    
    class Meta:
        verbose_name_plural = "Our Goal"


class ProductPaymentMethod(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    heading = models.ForeignKey(HeadingAndSubheading, on_delete=models.CASCADE,null=True)
    title = models.CharField(_("productPaymentMethodTitle"),max_length=250)
    content = models.TextField(_("productPaymentMethodContent"))
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)
    
    def __str__(self):
        return '{}'.format(self.title)

class ProductFunctionality(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    heading = models.ForeignKey(HeadingAndSubheading, on_delete=models.CASCADE,null=True)
    title = models.CharField(_("productFunctionalitytitle"),max_length=250)
    content = models.TextField(_("productFunctionalitycontent"))
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)
    
    def __str__(self):
        return '{}'.format(self.title)

class AboutProduct(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(_("aboutProductTitle"),max_length=250)
    content = models.TextField(_("aboutProductContent"))
    image = models.ImageField(_("aboutProductImage"),upload_to='about_product')
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    def __str__(self):
        return '{}'.format(self.title)



# class Conclusion_section(models.Model):
#     product = models.ForeignKey(Product,on_delete=models.CASCADE)
#     title = models.CharField(_("title"),max_length=250)
#     content = models.TextField(_("content"))
#     image = models.ImageField(_("image"), upload_to="productImages")
#     created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
#     updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)
    
#     def __str__(self):
#         return '{}'.format(self.title)

