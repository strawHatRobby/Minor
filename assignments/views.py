from django.shortcuts import render
from pagedown.widgets import PagedownWidget
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (
    TemplateView,ListView,DetailView,
    CreateView,UpdateView,DeleteView
    )
# Create your views here.
from . import models

class AssignmentListView(LoginRequiredMixin,ListView):
    context_object_name = "assignments"
    model = models.Assignment
    
class AssignmentDetailView(LoginRequiredMixin,DetailView):
    model = models.Assignment
    
    

from django import forms

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = models.Assignment
        fields = ['title', 'content', 'marks', 'submission_date', 'subject_id']
        widgets = {
            'content': PagedownWidget(show_preview=True)
        }

class AssignmentCreateView(LoginRequiredMixin,CreateView):
    form_class = AssignmentForm
    model = models.Assignment
    
class AssignmentUpdateView(LoginRequiredMixin,CreateView):
    fields = ('title',
            'content',
            'file',
            'marks',
            'submission_date',
            'subject_id')
    model = models.Assignment
    
class AssignmentDeleteView(LoginRequiredMixin,DeleteView):
    model = models.Assignment
    success_url = reverse_lazy("assignment:list_assignment")
    
