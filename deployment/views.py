from django.shortcuts import render
from django.views.generic import View, ListView
from ServerAdministrator.views import LoginRequiredMixin
from deployment import models

__author__ = 'dracks'


class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'index.html')


class ApplicationListView(LoginRequiredMixin, ListView):
    model = models.Application
    template_name = "application/list.html"
