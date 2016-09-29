from __future__ import unicode_literals
import datetime
from django.db import models
from courses.models import Subject
# Create your models here.

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=False,deafult="")
    file = models.FileField(null=True)
    marks = models.IntegerField(default=0)
    time_stamp = models.DateTimeField(auto_now_add=True)
    submission_date = models.DateTimeField(default=datetime.datetime.now,blank=True)
    subject_id = models.ForeignKey(Subject)
    
    def __str__(self):
        return "{} for {} marks".format(self.title,self.marks)
        
class Question(models.Model):
    question = models.CharField(max_length=255)
    marks = models.IntegerField(default=0)
    order = models.IntegerField(default=0)
    assignment = models.ForeignKey(Assignment)
    
    class Meta:
        ordering = ['order',]
    
    def __str__(self):
        return self.question

class Answers(models.Model):
    question = models.ForeignKey(Question)
    answer = models.TextField(default='')
    correct = models.BooleanField(default=False)
    
    def __str__(self):
        return self.answer