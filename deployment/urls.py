from django.conf.urls import url
from deployment import views

__author__ = 'dracks'

urlpatterns = [
    url('^$', views.IndexView.as_view(), name="index"),
    url('^applications$', views.ApplicationListView.as_view(), name="application_list")
]