from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.shortcuts import render
from pagedown.widgets import PagedownWidget
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    TemplateView,ListView,DetailView,
    CreateView,UpdateView,DeleteView
    )
# Create your views here.
from . import models

class FormListView(ListView):
    context_object_name = "assignments"
    model = models.Form
    
class FormDetailView(DetailView):
    model = models.Form
    
    

from django import forms

class FormForm(forms.ModelForm):
    class Meta:
        model = models.Form
        fields = ['subject', 'content',  'user', 'comments']
        widgets = {
            'content': PagedownWidget(show_preview=True)
        }

class FormCreateView(CreateView):
    form_class = FormForm
    model = models.Form
    
class FormUpdateView(CreateView):
    fields = ('subject',
            'contents',
            'timestamp',
            'user',
            'comments',)
    model = models.Form
    
class FormDeleteView(DeleteView):
    model = models.Form
    success_url = reverse_lazy("assignment:list_assignment")
    


class CommentsListView(ListView):
    context_object_name = "assignments"
    model = models.Comments
    
class CommentsDetailView(DetailView):
    model = models.Comments
    


class CommentsForm(forms.ModelForm):
    class Meta:
        model = models.Comments
        fields = ['content', 'votes', 'posted_by']
        widgets = {
            'content': PagedownWidget(show_preview=True)
        }

class CommentsCreateView(CreateView):
    form_class = CommentsForm
    model = models.Comments
    
class CommentsUpdateView(CreateView):
    fields = ('content',
            'votes',
            'posted_by')
    model = models.Comments
    
class CommentsDeleteView(DeleteView):
    model = models.Comments
    success_url = reverse_lazy("assignment:list_assignment")