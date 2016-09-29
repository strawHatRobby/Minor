from __future__ import unicode_literals
import datetime
from django.db import models

# Create your models here.
    

class Course(models.Model):
    course_name = models.CharField(max_length=255,blank=False,unique=True)
    start_date = models.DateTimeField(default=datetime.datetime.now,blank=False)
    end_date = models.DateTimeField(default=datetime.datetime.now,blank=False)
    credits = models.IntegerField(default=0)
    
    def __str__(self):
        return self.course_name
    


class Subject(models.Model):
    subject_name = models.CharField(max_length=255,blank=False,unique=True)
    description = models.TextField(default='')
    syllabus = models.FileField(null=True,blank=True)
    credits = models.IntegerField(default=0)
    course = models.ForeignKey(Course)
    
    def __str__(self):
        return self.subject_name