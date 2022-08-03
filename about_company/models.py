from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify

# Create your models here.

class About(models.Model):
    name = models.CharField(_("name"), max_length=100)
    image = models.ImageField(_("image"),upload_to="about")
    slug = models.SlugField(_("aboutSlug"), max_length=100, blank=True)
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(About, self).save(*args, **kwargs)
       
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "About"
    
class ContactAddress(models.Model):
    office = models.CharField(_("officeName"),max_length=250,unique=True)
    location = models.TextField(_("officeLocation"))
    phone = models.CharField(_("officeNumbers"),max_length=500,help_text="use , seperator for officeNumber",blank=True,null=True,default="")
    email = models.CharField(_("officeEmails"),max_length=500,help_text="use , seperator for officeEmails",blank=True,null=True,default="")
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    def __str__(self):
        return "{}".format(self.office)

    class Meta:
        verbose_name_plural = "Contact Address"

class BecomeOurPartner(models.Model):
    first_name = models.CharField(_("firstName"),max_length=250)
    last_name = models.CharField(_("lastName"),max_length=250)
    email = models.EmailField(_("email"),max_length=250)
    contact = models.CharField(_("contactNumber"),max_length=250)
    address = models.TextField(_("address"),max_length=250)
    state = models.CharField(_("state"),max_length=250)
    city = models.CharField(_("city"),max_length=250)
    source = models.CharField(_("How did you hear from us "),max_length=250)
    source_optional = models.TextField(_("sourceOptional"),max_length=250,help_text="Optional")
    notes = models.TextField(_("notesOptional"),max_length=250,help_text="Optional")
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    def __str__(self):
        return "{},{}".format(self.first_name, self.last_name)
    
    class Meta:
        verbose_name_plural = "Become Our Partner"

class PrivacyPolicy(models.Model):
    title = models.CharField(_("privacyPolicyTitle"),default="Privacy Policy",max_length=100)
    description = models.TextField(_("privacyPolicyDescription"))
    content = RichTextUploadingField(_("privacyPolicyContent"),blank=True,null=True)
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    def __str__(self):
        return "{}".format(self.title)
    
    class Meta:
        verbose_name_plural = "Privacy Policy"

    
class TermsAndCondition(models.Model):
    title = models.CharField(_("termAndConditionTitle"),default="Term & Condition",max_length=100)
    description = models.TextField(_("termAndConditionDescription"))
    content = RichTextUploadingField(_("termAndConditionContent"),blank=True,null=True)
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)
    
    
    def __str__(self):
        return "{}".format(self.title)
    
    class Meta:
        verbose_name_plural = "Terms & Condition"


