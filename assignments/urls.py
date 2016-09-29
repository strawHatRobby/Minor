from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
urlpatterns = [
    url(r'^assignment_list/$',views.AssignmentListView.as_view(), name='list_assignment'),
    url(r'^assignment_list/(?P<pk>\d+)/$',views.AssignmentDetailView.as_view(), name='detail_assignment'),
    # url(r'^assignment_list/(?P<pk>\d+)/$',views.RetrieveUpdateDestroyAssignment.as_view(), name='update_assignment'),
    ]