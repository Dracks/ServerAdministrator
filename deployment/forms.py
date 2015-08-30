from django.forms import forms

__author__ = 'dracks'


class VersionFromZipForm(forms.Form):
    file = forms.FileField