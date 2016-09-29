from django.conf.urls import url,include
from courses import views
urlpatterns = [
    url(r'^assignments/',include('assignments.urls',namespace='assignments')),
    url(r'^subject_list/$',views.SubjectListView.as_view(), name='list_subject'),
    url(r'^subject_list/(?P<pk>\d+)/$',views.SubjectDetailView.as_view(), name='detail_subject'),
    ]