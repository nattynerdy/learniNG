from django.db import models
from django.conf import settings
from tags.models import Tag

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name = "courses")
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="courses",
        on_delete=models.CASCADE
    )
    progress = models.DecimalField(decimal_places = 2, db_default = 0.0 )
    page = models.IntegerField(db_default = 1)