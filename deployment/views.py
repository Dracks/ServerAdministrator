from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView, DetailView, TemplateView
from django.views.generic.edit import FormView, DeleteView
from ServerAdministrator.views import LoginRequiredMixin
from deployment import models, forms
from django.views.generic import edit
from django.http import HttpResponseRedirect

import zipfile

__author__ = 'dracks'

APP_ID_KEY = 'application_pk'

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
    template_name = "version/list.html"

    def get_queryset(self):
        self.application = get_object_or_404(models.Application, pk=self.kwargs[APP_ID_KEY])
        return models.Version.objects.filter(application_id=self.application.id).order_by('creation').reverse()

    def get_context_data(self, **kwargs):
        context = super(VersionListView, self).get_context_data(**kwargs)
        context['application'] = self.application
        return context

class VersionNewFromZipView(LoginRequiredMixin, FormView):
    form_class = forms.VersionFromZipForm
    template_name = 'version/zip_new.html'

    def get_context_data(self, **kwargs):
        application = get_object_or_404(models.Application, pk=self.kwargs[APP_ID_KEY])
        context = super(VersionNewFromZipView, self).get_context_data(**kwargs)
        context['application'] = application
        return context

    def form_valid(self, form):
        app = models.Application.objects.get(pk=form['application'].value())
        print(form['application'].value())
        file = zipfile.ZipFile(form['file'].value())
        version = models.Version.create_from_zip(app, file)
        version.save()
        return HttpResponseRedirect(reverse('deployment:version_draft', args=[version.pk]))

    def post(self, request, *args, **kwargs):
        return super(VersionNewFromZipView, self).post(request, *args, **kwargs)

class VersionDraftView(LoginRequiredMixin, DetailView):
    model = models.Version
    template_name = "version/draft.html"

    def get_context_data(self, **kwargs):
        version = self.get_object()
        files = models.VersionFile.objects.filter(version=version.pk).values('pk', 'name', 'path')
        context = super(VersionDraftView, self).get_context_data(**kwargs)
        context['files'] = files
        return context

class VersionDeleteDraftView(LoginRequiredMixin, DeleteView):
    model = models.Version
    template_name = "version/delete.html"
    queryset = models.Version.objects.filter(is_draft=True)

    def get_success_url(self):
        app = self.get_object().application
        return reverse('deployment:version_list', args=[app.pk])

class ChangeFileAddView(LoginRequiredMixin, FormView):
    model = models.VersionFile


