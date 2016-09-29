from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class LoginPageView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self,**kwargs):
        context = super(LoginPageView,self).get_context_data(**kwargs)
        context["fake_data"] = "fakeing it"
        return context