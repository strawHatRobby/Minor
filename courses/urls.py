from django.conf.urls import url,include
from courses.models import Course
from django.core.urlresolvers import reverse_lazy
from courses import views
urlpatterns = [
    url(r'^subject_list/$',views.SubjectListView.as_view(), name='list_subject'),
    url(r'^subject_list/(?P<pk>\d+)/$',views.SubjectDetailView.as_view(), name='detail_subject'),
    url(r'^create_subject/$',views.SubjectCreateView.as_view(), name='create_subject'),
    url(r'^edit_subject/(?P<pk>\d+)/$',views.SubjectUpdateView.as_view(), name='edit_subject'),
    url(r'^delete_subject/(?P<pk>\d+)/$',views.SubjectDeleteView.as_view(), name='delete_subject'),
    url(r'^course_list/$',views.CourseListView.as_view(), name='list_course'),
    url(r'^course_list/(?P<pk>\d+)/$',views.CourseDetailView.as_view(), name='detail_course'),
    url(r'^create_course/$',views.CourseCreateView.as_view(model=Course, success_url=reverse_lazy('course:list_course')), name='create_course'),
    url(r'^edit_course/(?P<pk>\d+)/$',views.CourseUpdateView.as_view(model=Course, success_url=reverse_lazy('course:list_course')), name='edit_course'),
    url(r'^delete_course/(?P<pk>\d+)/$',views.CourseDeleteView.as_view(model=Course, success_url=reverse_lazy('course:list_course')), name='delete_course'),
    # url(r'^assignment_list/(?P<pk>\d+)/$',views.RetrieveUpdateDestroyAssignment.as_view(), name='update_course'),
    ]