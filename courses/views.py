from django.shortcuts import render
from rest_framework import generics
from assignments.models import Assignment,Question,Answers
from courses.models import Course,Subject
from forums.models import Form,Comments
from schools.models import School
# Create your views here.
