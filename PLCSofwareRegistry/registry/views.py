from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from .forms import RegistryForm, UserRegForm, UserAuthForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from .models import Software
def home(request: HttpRequest):
    print(request.user)
    if request.user.id is None:
        context = {'user': request.user,
                   'sw': []}
        return render(request, 'registry/home.html', context)
    context = {'user': request.user,
               'sw': Software.objects.filter(creator=request.user.id)}
    return render(request, 'registry/home.html', context)

def add_software(request: HttpRequest):
    form = RegistryForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        form1 = form.save()
    return render(request, 'registry/add.html', locals())

def error404(request: HttpRequest, exception):
    return render(request, 'registry/error404.html', locals())

def user_logout(request):
    logout(request)
    return HttpResponse("<h3>Вы успешно вышли из системы</h3><a href=\"..\"><button>home</button></a>")

def user_login(request: HttpRequest):
    form = UserAuthForm(request.POST or None)
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is None:
            return HttpResponse('<h1>Его нет в списке</h1>')
        login(request, user)
        return HttpResponse("<h3>Вы успешно вощли</h3><a href=\"..\"><button>home</button></a>")
    return render(request, 'registry/log.html', locals())

def user_registration(request):
    form = UserRegForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        form1 = form.save()

        return HttpResponse("<h3>Вы успешно зарегистрировались</h3><a href=\"..\"><button>home</button></a>")
    return render(request, 'registry/reg.html', locals())
