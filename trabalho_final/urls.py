"""
URL configuration for trabalho_final project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from home.views import IndexView

admin.site.site_header = "Controle de Acesso"
admin.site.index_title = "Gerencimaneto de Chaves - Controle de Acesso"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('bloco.urls')),
    path('', include('sala.urls')),
    path('', include('professor.urls')),
    path('', include('funcionario.urls')),
    path('', include('chavebloco.urls')),
    path('', include('chavesala.urls')),
    path('', include('retiradabloco.urls')),
    path('', include('retiradablocop.urls')),
    path('', include('retiradasalafunc.urls')),
    path('', include('retiradasalaprof.urls')),

]
