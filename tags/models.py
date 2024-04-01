from django.db import models
from colorfield.fields import ColorField

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)
    color = ColorField()
