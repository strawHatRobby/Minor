from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
# Create your views here.
from . import models

class AssignmentListView(ListView):
    context_object_name = "assignments"
    model = models.Assignment
    
class AssignmentDetailView(DetailView):
    model = models.Assignment
    
