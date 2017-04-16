from django.conf.urls import url,include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^assignments/',include('assignments.urls',namespace='assignments')),
    url(r'^course_list/$',views.ListCreateCourse.as_view(), name='course_list'),
    url(r'^course_list/(?P<pk>\d+)/$',views.RetrieveUpdateDestroyCourse.as_view(), name='course_update'),
    url(r'^assignment_list/$',views.ListCreateAssignment.as_view(), name='assignment_list'),
    url(r'^assignment_list/(?P<pk>\d+)/$',views.RetrieveUpdateDestroyAssignment.as_view(), name='assignment_update'),
    url(r'^subject_list/$',views.ListCreateSubject.as_view(), name='subject_list'),
    url(r'^subject_list/(?P<pk>\d+)/$',views.RetrieveUpdateDestroySubject.as_view(), name='subject_update'),
    url(r'^school_list/$',views.ListCreateSchool.as_view(), name='school_list'),
    url(r'^school_list/(?P<pk>\d+)/$',views.RetrieveUpdateDestroySchool.as_view(), name='school_update'),
    url(r'^question_list/$',views.ListCreateQuestion.as_view(), name='question_list'),
    url(r'^question_list/(?P<pk>\d+)/$',views.RetrieveUpdateDestroyQuestion.as_view(), name='question_update'),
    ]
    
urlpatterns = format_suffix_patterns(urlpatterns)