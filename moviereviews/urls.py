from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from usuarios.views import foro  

def home(request):
    return HttpResponse("<h1>Bienvenido a MovieReviews</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('', home, name='home'),  # Página de inicio
    path('foro/', foro, name='foro'),  # Página del foro
]
