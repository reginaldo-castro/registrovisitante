"""controle_visitantes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from dashboard.views import index
import usuarios.views
import visitantes.views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("", index, name="index"),
    path("registrar-visitante/", visitantes.views.registrar_visitante, name="registrar_visitante"),
    path("visitante/<int:id>/", visitantes.views.informacoes_visistantes, name="informacoes_visitante"),
    path('visitantex/<int:id>/finalizar-visita', visitantes.views.finalizar_visita, name='finalizar_visita'),
]
