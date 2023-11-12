
from django.contrib import admin
from django.urls import path, include

from registry.views import error404

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registry.urls'))
]

handler404 = error404
