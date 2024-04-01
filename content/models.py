from django.db import models
from django.conf import settings
from courses.models import Course

# Create your models here.
class Content(models.Model):
    number = models.IntegerField()
    course = models.ForeignKey(
        Course,
        related_name="content",
        on_delete=models.CASCADE,
        null=True
    )
    link = models.URLField()
    name = models.CharField(max_length = 100)