from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView, DetailView
from django.views.generic.edit import FormMixin
from ServerAdministrator.views import LoginRequiredMixin
from deployment import models, forms
from django.views.generic import edit

__author__ = 'dracks'


class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'index.html')


class ApplicationListView(LoginRequiredMixin, ListView):
    model = models.Application
    template_name = "application/list.html"

class ApplicationNewView(LoginRequiredMixin, edit.CreateView):
    model = models.Application
    template_name = "application/detail.html"
    fields = ['name']
    initial = {'name':''}

    def get_success_url(self):
        return reverse('deployment:application_list')

class ApplicationView(LoginRequiredMixin, edit.UpdateView):
    model = models.Application
    template_name = "application/detail.html"
    fields = ['name']

    def get_success_url(self):
        return reverse('deployment:application_list')


class VersionListView(LoginRequiredMixin, ListView):
    model = models.Version
    APP_ID_KEY = 'application_id'
    template_name = "version/list.html"

    def get_queryset(self):
        application = get_object_or_404(models.Application, pk=self.kwargs[self.APP_ID_KEY])
        return models.Version.objects.filter(application_id=application.id)

    def get_context_data(self, **kwargs):
        context = super(VersionListView, self).get_context_data(**kwargs)
        context['current_app_id'] = self.kwargs[self.APP_ID_KEY]
        return context

class VersionNewFromZipView(LoginRequiredMixin, FormMixin, DetailView):
    form_class = forms.VersionFromZipForm

    def post(self, request):
        pass