from __future__ import unicode_literals

from django.db import models
from courses.models import Course
# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=255)
    board = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)
    course = models.ManyToManyField(Course)
    
    def __str__(self):
        return self.name