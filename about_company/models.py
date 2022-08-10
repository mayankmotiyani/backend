from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify

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
    
class AboutCompany(models.Model):
    heading = models.CharField(max_length=100,null=True,blank=True,default="")
    description = models.TextField(_("aboutCompany"))
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    def __str__(self):
        return "About Us"

    class Meta:
        verbose_name_plural = "About Company"

class UnmatchedServices(models.Model):
    heading = models.ForeignKey(HeadingAndSubheading,on_delete=models.CASCADE)
    description = models.TextField(_("aboutCompany"))
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    def __str__(self):
        return "About Us Section 1"
    
    class Meta:
        verbose_name_plural = "8+ Years of unmatched Services"

class BlockchainForBusiness(models.Model):
    heading = models.ForeignKey(HeadingAndSubheading,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="blockchain_for_business")
    title = models.CharField(max_length=250,null=True,blank=True)
    description = models.TextField(_("aboutCompany"))
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)
    
    class Meta:
        verbose_name_plural = "Blockchain For Business"


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

class VisionAndMission(models.Model):
    heading = models.ForeignKey(HeadingAndSubheading,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="vision_and_mission")
    description = RichTextUploadingField(_("mission&vision"),blank=True,null=True)
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)

    def __str__(self):
        return "Vision And Mission"
    
    class Meta:
        verbose_name_plural = "Vision And Mission"
    
    
class Partners(models.Model):
    heading = models.ForeignKey(HeadingAndSubheading,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="Partners")
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)
    
   
    def __str__(self):
        return "Partners"

    class Meta:
        verbose_name_plural = "Partner"

class FAQs(models.Model):
    question= models.TextField(_("question"),blank=True,null=True)
    answer= models.TextField(_("answer"),blank=True,null=True)
    created_at = models.DateTimeField(_("creationDate"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updatedDate"),auto_now=True)
    
    def __str__(self):
        return "{}".format(self.question)
    
    class Meta:
        verbose_name_plural = "FAQ"