from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.registry, name='registry'),
    path('add/', views.add_software, name='add'),
]
