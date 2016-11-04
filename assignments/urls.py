from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.decorators import login_required, permission_required
from . import views
urlpatterns = [
    url(r'^assignment_list/$',views.AssignmentListView.as_view(), name='list_assignment'),
    url(r'^assignment_list/(?P<pk>\d+)/$',views.AssignmentDetailView.as_view(), name='detail_assignment'),
    url(r'^create_assignment/$',permission_required('assignments.can_add_assignment')(views.AssignmentCreateView.as_view()), name='create_assignment'),
    url(r'^edit_assignment/(?P<pk>\d+)/$',permission_required('assignments.can_change_assignment')(views.AssignmentUpdateView.as_view()), name='edit_assignment'),
    url(r'^delete_assignment/(?P<pk>\d+)/$',permission_required('assignments.can_delete_assignment')(views.AssignmentDeleteView.as_view()), name='delete_assignment'),
    url(r'^create_assignment_sms/$',views.create_assignment_sms, name="create_assignment_sms" ),
    url(r'^update_assignment_sms/$',views.update_assignment_sms, name="update_assignment_sms" ),
    # url(r'^assignment_list/(?P<pk>\d+)/$',views.RetrieveUpdateDestroyAssignment.as_view(), name='update_assignment'),
    ]