from django.shortcuts import render
from rest_framework import generics
from assignments.models import Assignment,Question,Answers
from courses.models import Course,Subject
from forums.models import Form,Comments
from schools.models import School
from pagedown.widgets import PagedownWidget
from django.core.urlresolvers import reverse_lazy
# Create your views here.
from django import forms
from . import models 
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView
# Create your views here.


class SubjectListView(LoginRequiredMixin,ListView):
    context_object_name = "subjects"
    model = Subject
    
class SubjectDetailView(LoginRequiredMixin,DetailView):
    model = Subject
    
class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('subject_name', 'description', 'syllabus', 'credits', 'course')
        widgets = {
            'content': PagedownWidget(show_preview=True)
        }

class SubjectCreateView(LoginRequiredMixin,CreateView):
    form_class = SubjectForm
    model = models.Subject
    
class SubjectUpdateView(LoginRequiredMixin,CreateView):
    fields = ('subject_name',
            'description',
            'syllabus',
            'credits',
            'course')
    model = models.Subject
    
class SubjectDeleteView(LoginRequiredMixin,DeleteView):
    model = models.Subject
    success_url = reverse_lazy
    success_url = reverse_lazy("subject:list_subject")
    
    

class CourseListView(LoginRequiredMixin,ListView):
    context_object_name = "courses"
    model = Course
    
class CourseDetailView(DetailView):
    model = Course
    
class CourseForm(LoginRequiredMixin,forms.ModelForm):
    class Meta:
        model = Course
        fields = ('course_name', 'start_date', 'end_date', 'credits')
        widgets = {
            
        }

class CourseCreateView(LoginRequiredMixin,CreateView):
    form_class = CourseForm
    model = models.Course
    
class CourseUpdateView(LoginRequiredMixin,CreateView):
    fields = ('course_name',
            'start_date',
            'end_date',
            'credits')
    model = models.Course
    
class CourseDeleteView(LoginRequiredMixin,DeleteView):
    model = models.Course
    success_url = reverse_lazy
    success_url = reverse_lazy("course:list_course")

    
