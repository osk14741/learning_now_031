from django.apps import apps
from django import forms
from django.contrib import auth

from blog.models import Document, UserDefinedCode


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        exclude = ('code',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', '')
        super(DocumentForm, self).__init__(*args, **kwargs)
        self.fields['user_defined_code'] = forms.ModelChoiceField(queryset=UserDefinedCode.objects.filter(owner=user))
        self.fields['unique_code'] = forms.CharField(max_length=15)


