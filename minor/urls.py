"""minor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$',views.home),
    url(r'^admin/', admin.site.urls),
    url(r'^auth/',include('accounts.urls',namespace='auth')),
    url(r'^schools/',include('schools.urls',namespace='school')),
    url(r'^assignments/',include('assignments.urls',namespace='assignment')),
    url(r'^courses/',include('courses.urls',namespace='course')),
    url(r'^api/v1/courses/',include('rest_api.urls',namespace='rest_api')),
    url(r'^api_auth/',include('rest_framework.urls',namespace='rest_framework')),
]
