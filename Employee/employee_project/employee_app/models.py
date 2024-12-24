from django.db import models

# Create your models here.
class Field(models.Model):
    Name = models.CharField(max_length=20, default='')
    Email = models.CharField(max_length=40,default='')
    Department = models.CharField(max_length=50, default='')
    Date_of_joining = models.DateField(default='')