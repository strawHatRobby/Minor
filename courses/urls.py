from django.conf.urls import url,include
from courses import views
urlpatterns = [
    url(r'^assignments/',include('assignments.urls',namespace='assignments')),
    ]