from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.widgets import CKEditorWidget

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=200)
  
    querry = RichTextField(blank=True, null=True)
   
    email =models.EmailField(max_length=200)
    title= models.CharField(max_length=200)