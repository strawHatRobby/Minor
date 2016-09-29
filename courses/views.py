from django.shortcuts import render
from rest_framework import generics
from assignments.models import Assignment,Question,Answers
from courses.models import Course,Subject
from forums.models import Form,Comments
from schools.models import School
# Create your views here.
from django.views.generic import TemplateView

from django.views.generic import TemplateView,ListView,DetailView
# Create your views here.


class SubjectListView(ListView):
    context_object_name = "subjects"
    model = Subject
    
class SubjectDetailView(DetailView):
    model = Subject