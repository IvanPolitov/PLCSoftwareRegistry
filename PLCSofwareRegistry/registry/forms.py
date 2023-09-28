from django import forms
from .models import *

class RegistryForm(forms.ModelForm):

    class Meta:
        model = Software
        exclude = ['']
