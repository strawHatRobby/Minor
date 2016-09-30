from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
# class LoginPageView(TemplateView):
#     template_name = 'home.html'
    
#     def get_context_data(self,**kwargs):
#         context = super(LoginPageView,self).get_context_data(**kwargs)
#         context["fake_data"] = "fakeing it"
#         return context

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.contrib.auth import login, logout
# Create your views here.

    

class LoginPageView(generic.FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy("assignment:list_assignment")
    template_name = "home.html"
    
    def get_form(self,form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(self.request,**self.get_form_kwargs())    

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginPageView,self).form_valid(form)
        
class LogoutView(generic.RedirectView):
    url = reverse_lazy("profile")
    template_name = "logout.html"
    
    def get(self,request,*args,**kwargs):
        logout(request)
        return super(LogoutView,self).get(request,*args,**kwargs)