from django import forms
from deployment import models

__author__ = 'dracks'


class VersionFromZipForm(forms.Form):
    application = forms.ModelChoiceField(queryset=models.Application.objects.all())
    file = forms.FileField()

    def is_valid(self):
        ret = super(VersionFromZipForm, self).is_valid()
        return ret