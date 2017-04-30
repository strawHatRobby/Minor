from django.shortcuts import render, get_object_or_404
from datetime import datetime
from pagedown.widgets import PagedownWidget
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    TemplateView,ListView,DetailView,
    CreateView,UpdateView,DeleteView
    )
# Create your views here.
from . import models
from minor import settings
from datetime import datetime

from twilio.rest import TwilioRestClient
import string

class AssignmentListView(ListView):
    context_object_name = "assignments"
    model = models.Assignment
    
class AssignmentDetailView(DetailView):
    model = models.Assignment
    
    

from django import forms

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = models.Assignment
        fields = ['title', 'content', 'marks', 'submission_date', 'subject_id']
        widgets = {
            'content': PagedownWidget(show_preview=True)
        }
    
   

class AssignmentCreateView(CreateView):
    form_class = AssignmentForm
    model = models.Assignment
    success_url = reverse_lazy("assignment:create_assignment_sms")
    

    
def create_assignment_sms(request):
    sms_string = models.Assignment.objects.all().order_by('-id')[0].__str__()
    sms_string = string.replace(sms_string,'<','')
    sms_string = string.replace(sms_string,'>','')
    client = TwilioRestClient(account=settings.TWILIO_ACCOUNT_SID,
                            token=settings.TWILIO_AUTH_TOKEN)
    client.messages.create(from_="(651) 314-1235" ,
                        to = ["+919821157535","+919911449771"],
                        body="You have a new assignment : {}".format(sms_string))
    return HttpResponseRedirect(reverse_lazy("assignment:list_assignment"))
        
    
def update_assignment_sms(request):
    # sms_string = get_object_or_404(models.Assignment, id=id)
    # sms_string = string.replace(sms_string,'<','')
    # sms_string = string.replace(sms_string,'>','')
    # client = TwilioRestClient(account=settings.TWILIO_ACCOUNT_SID,
    #                         token=settings.TWILIO_AUTH_TOKEN)
    # client.messages.create(from_="(651) 314-1235" ,
    #                     to = ["+919821157535"],
    #                     body="assignment {} has been updated".format(sms_string))
    return HttpResponseRedirect(reverse_lazy("assignment:list_assignment"))
    
    
class AssignmentUpdateView(CreateView):
    fields = ('title',
            'content',
            'file',
            'marks',
            'submission_date',
            'subject_id')
    model = models.Assignment
    success_url = reverse_lazy("assignment:update_assignment_sms")
    
class AssignmentDeleteView(DeleteView):
    model = models.Assignment
    success_url = reverse_lazy("assignment:list_assignment")
    
