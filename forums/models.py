from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Comments(models.Model):
    content = models.TextField(default='')
    votes = models.IntegerField(default=0)
    posted_by = models.ForeignKey(User)
    
    def __str__(self):
        return "posted by {}".format(self.posted_by)
    
class Form(models.Model):
    subject = models.CharField(max_length=255)
    content = models.TextField(default='')
    timestamp = models.DateTimeField(auto_now_add=True)
    solved = models.BooleanField(default=False)
    user = models.ManyToManyField(User)
    comments = models.ForeignKey(Comments)
    
    def __str__(self):
        return self.subject