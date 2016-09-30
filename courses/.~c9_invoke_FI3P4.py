from django.shortcuts import render
from rest_framework import generics
from assignments.models import Assignment,Question,Answers
from courses.models import Course,Subject
from forums.models import Form,Comments
from schools.models import School
from pagedown.widgets import PagedownWidget
from django.core.urlresolvers import reverse_lazy
# Create your views here.
from . import Mode 
from . import models 
from django.views.generic import TemplateView

from django.views.generic import TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView
# Create your views here.


class SubjectListView(ListView):
    context_object_name = "subjects"
    model = Subject
    
class SubjectDetailView(DetailView):
    model = Subject
    
class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('subject_name', 'description', 'syllabus', 'credits', 'course')
        widgets = {
            'content': PagedownWidget(show_preview=True)
        }

class SubjectCreateView(CreateView):
    form_class = SubjectForm
    model = models.Subject
    
class SubjectUpdateView(CreateView):
    fields = ('subject_name',
            'description',
            'syllabus',
            'credits',
            'course')
    model = models.Subject
    
class SubjectDeleteView(DeleteView):
    model = models.Subject
    success_url = reverse_lazy
    success_url = reverse_lazy("subject:list_subject")
    
    

class CourseListView(ListView):
    context_object_name = "courses"
    model = Subject
    
class CourseDetailView(DetailView):
    model = Subject
    
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('course_name', 'start_date', 'end_date', 'credits']
        widgets = {
            
        }

class CourseCreateView(CreateView):
    form_class = CourseForm
    model = models.Subject
    
class CourseUpdateView(CreateView):
    fields = ('course_name',
            'start_date',
            'end_date',
            'credits')
    model = models.Subject
    
