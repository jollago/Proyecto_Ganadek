"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from tasks import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup ,name='signup'),
    path('Panel Informativo/', views.PanelInformativo ,name='PanelInformativo'),
    path('profile/', views.profile ,name='profile'),
    path('password-change/', views.password_change, name='password_change'),
    path('logout/', views.signout ,name='logout'),
    path('signin/', views.signin ,name='signin'),
    path('fincas/', views.listar_fincas, name='listar_fincas'),
    path('fincas/nueva/', views.crear_finca, name='crear_finca'),
    path('fincas/editar/<int:finca_id>/', views.editar_finca, name='editar_finca'),
    path('fincas/eliminar/<int:finca_id>/', views.eliminar_finca, name='eliminar_finca'),
]
 