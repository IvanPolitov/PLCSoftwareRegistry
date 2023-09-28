from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .forms import RegistryForm
def registry(request: HttpRequest):
    return render(request, 'registry/registry.html')


def add_software(request: HttpRequest):
    form = RegistryForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        form1 = form.save()
    return render(request, 'registry/add.html', locals())
