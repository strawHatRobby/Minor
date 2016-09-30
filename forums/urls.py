from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
urlpatterns = [
    url(r'^form_list/$',views.FormListView.as_view(), name='list_from'),
    url(r'^form_list/(?P<pk>\d+)/$',views.FormDetailView.as_view(), name='detail_form'),
    url(r'^create_form/$',views.FormCreateView.as_view(), name='create_form'),
    url(r'^edit_form/(?P<pk>\d+)/$',views.FormUpdateView.as_view(), name='edit_form'),
    url(r'^delete_form/(?P<pk>\d+)/$',views.FormDeleteView.as_view(), name='delete_form'),
    # url(r'^assignment_list/(?P<pk>\d+)/$',views.RetrieveUpdateDestroyAssignment.as_view(), name='update_assignment')
    ]