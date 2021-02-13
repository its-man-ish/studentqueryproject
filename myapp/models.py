from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=200)
    querry = RichTextField(blank=True, null=True)
    email =models.EmailField(max_length=200)