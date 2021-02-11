from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=200)
    querry = models.TextField(max_length=500)
    email =models.EmailField(max_length=200)