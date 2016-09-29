from django.conf.urls import url,include

urlpatterns = [
    url(r'^assignments/',include('assignments.urls',namespace='assignments')),
    ]