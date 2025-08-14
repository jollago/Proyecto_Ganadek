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
from django.contrib.auth import views as auth_views
from django.urls import path




urlpatterns = [
    
    path('signin/', views.signin ,name='signin'),
    
    
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup ,name='signup'),
    path('Panel Informativo/', views.PanelInformativo ,name='PanelInformativo'),
    path('profile/', views.profile ,name='profile'),
    path('profile/gestion_usuarios/', views.gestion_usuarios, name='gestion_usuarios'),
    path('password-change/', views.password_change, name='password_change'),
    path('logout/', views.signout ,name='logout'),
    

    
    # Lista de fincas
    path('Fincas/', views.FincaListView.as_view(), name='finca_list'),
    
    # Detalle de finca
    path('Fincas/<int:pk>/', views.FincaDetailView.as_view(), name='finca_detail'),
    
    # Crear finca
    path('Fincas/crear/', views.FincaCreateView.as_view(), name='finca_create'),
    
    # Editar finca
    path('Fincas/<int:pk>/editar/', views.FincaUpdateView.as_view(), name='finca_edit'),
    
    # Eliminar finca
    path('Fincas/eliminar/<int:pk>/', views.FincaDeleteView.as_view(), name='finca_delete'),
    
    
    # ============= URLs PARA POTREROS =============
    
    # Lista de potreros
    path('UnidadProductiva/', views.UnidadProductivaListView.as_view(), name='UnidadProductiva_list'),
    
    # Detalle de potrero
    path('UnidadProductiva/<int:pk>/', views.UnidadProductivaDetailView.as_view(), name='UnidadProductiva_detail'),
    
    # Crear potrero
    path('UnidadProductiva/crear/', views.UnidadProductivaCreateView.as_view(), name='UnidadProductiva_create'),
    
    # Editar potrero
    path('UnidadProductiva/<int:pk>/editar/', views.UnidadProductivaUpdateView.as_view(), name='UnidadProductiva_edit'),
    
    # Eliminar potrero
    path('UnidadProductiva/<int:pk>/eliminar/', views.UnidadProductivaDeleteView.as_view(), name='UnidadProductiva_delete'),
    
    # ============= URLs PARA ANIMALES =============

    # Lista de animales
    path('Animal/', views.AnimalListView.as_view(), name='animal_list'),

    # Detalle de animal
    path('Animal/<int:pk>/', views.AnimalDetailView.as_view(), name='animal_detail'),

    # Crear animal
    path('Animal/crear/', views.AnimalCreateView.as_view(), name='animal_create'),

    # Editar animal
    path('Animal/<int:pk>/editar/', views.AnimalUpdateView.as_view(), name='animal_edit'),

    # Eliminar animal
    path('Animal/<int:pk>/eliminar/', views.AnimalDeleteView.as_view(), name='animal_delete'),
]
