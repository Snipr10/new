from django.db import models

from django.utils.html import mark_safe

# Create your models here.
class UserInfo(models.Model):
    upload = models.ImageField(upload_to ='uploads', null=True, blank=True)

    first_name = models.CharField(max_length=32, null=True, blank=True)
    second_name = models.CharField(max_length=32, null=True, blank=True)
    dob = models.DateField()

    def User_preview(self):
        return mark_safe(f'<img src = "{self.upload.url}" width = "100"/>')

    def User_photo(self):
        return mark_safe(f'<img src = "{self.upload.url}" width = "300"/>')

    def __str__(self):
        return self.first_name + " " + self.second_name

