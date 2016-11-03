from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
def home(request):
    return HttpResponseRedirect(reverse('auth:login'))
    