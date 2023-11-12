from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='registry'),
    path('add/', views.add_software, name='add'),
    path('reg/', views.user_registration, name='user_registration'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
]


