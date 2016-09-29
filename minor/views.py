from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

def home(request):
    return HttpResponseRedirect(reverse('auth:login'))
    