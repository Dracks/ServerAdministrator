"""ServerAdministrator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from oauth2_provider import views as oauth_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name':'login.html'}),
    url(r'^accounts/logout/$','django.contrib.auth.views.logout'),
    #url(r'^oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^oauth/authorize/$', oauth_views.AuthorizationView.as_view(), name="authorize"),
    url(r'^oauth/token/$', oauth_views.TokenView.as_view(), name="token"),
    url(r'^oauth/revoke_token/$', oauth_views.RevokeTokenView.as_view(), name="revoke-token"),
    url(r'^api/', include('rest.urls'))
]
