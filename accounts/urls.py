from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
urlpatterns = [
    url(r'^login/',views.LoginPageView.as_view(),name='login'),
    ]