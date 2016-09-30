from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django.shortcuts import render
from pagedown.widgets import PagedownWidget
from schools.models import School
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    TemplateView,ListView,DetailView,
    CreateView,UpdateView,DeleteView
    )
# Create your views here.
from . import models

class SchoolListView(ListView):
    context_object_name = "assignments"
    model = models.School
    
class SchoolDetailView(DetailView):
    model = models.School
    
    

from django import forms

class SchoolForm(forms.ModelForm):
    class Meta:
        model = models.School
        fields = ['name', 'board', 'location', 'rating', 'course']
        widgets = {
            
        }

class SchoolCreateView(CreateView):
    form_class = SchoolForm
    model = models.School
    
class SchoolUpdateView(CreateView):
    fields = ('name',
            'board',
            'location',
            'rating',
            'course')
    model = models.School
    
class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("assignment:list_assignment")
    
