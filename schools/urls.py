from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
urlpatterns = [
    url(r'^school_list/$',views.SchoolListView.as_view(), name='list_school'),
    url(r'^school_list/(?P<pk>\d+)/$',views.SchoolDetailView.as_view(), name='detail_school'),
    url(r'^create_school/$',views.SchoolCreateView.as_view(), name='create_school'),
    url(r'^edit_school/(?P<pk>\d+)/$',views.SchoolUpdateView.as_view(), name='edit_school'),
    url(r'^delete_school/(?P<pk>\d+)/$',views.SchoolDeleteView.as_view(), name='delete_school'),
    # url(r'^assignment_list/(?P<pk>\d+)/$',views.RetrieveUpdateDestroyAssignment.as_view(), name='update_assignment'),
    ]