from django.conf.urls import url
from deployment import views

__author__ = 'dracks'

urlpatterns = [
    url('^$', views.IndexView.as_view(), name="index"),
    url('^applications$', views.ApplicationListView.as_view(), name="application_list"),
    url('^application/new/$', views.ApplicationNewView.as_view(), name="application_new"),
    url('^application/(?P<pk>[0-9]+)/$', views.ApplicationView.as_view(), name="application_edit"),
    url('^versions/(?P<application_pk>[0-9]+)/$', views.VersionListView.as_view(), name="version_list"),
    url('^version/(?P<application_pk>[0-9]+)/new/$', views.VersionNewFromZipView.as_view(), name="version_zip_new"),
    url('^version/(?P<pk>[0-9]+)/draft', views.VersionDraftView.as_view(), name="version_draft")
]