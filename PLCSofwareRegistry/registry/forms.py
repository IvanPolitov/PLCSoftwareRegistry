from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
class RegistryForm(forms.ModelForm):
    class Meta:
        model = Software
        exclude = ['']

class UserRegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',
                  'password1',
                  'password2']


class UserAuthForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username',
                  'password1',
                  'password2']