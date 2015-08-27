from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.shortcuts import render
from oauth2_provider.views import ProtectedResourceView
from oauth2_provider.views.mixins import ProtectedResourceMixin

__author__ = 'dracks'

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls):
        return login_required(super(LoginRequiredMixin, cls).as_view())


class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'navigation.html')