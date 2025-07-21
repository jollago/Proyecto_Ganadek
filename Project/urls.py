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
    
    # Lista de fincas
    path('Fincas/', views.FincaListView.as_view(), name='finca_list'),
    
    # Detalle de finca
    path('Fincas/<int:pk>/', views.FincaDetailView.as_view(), name='finca_detail'),
    
    # Crear finca
    path('Fincas/crear/', views.FincaCreateView.as_view(), name='finca_create'),
    
    # Editar finca
    path('Fincas/<int:pk>/editar/', views.FincaUpdateView.as_view(), name='finca_edit'),
    
    # Eliminar finca
    path('Fincas/<int:pk>/eliminar/', views.FincaDeleteView.as_view(), name='finca_delete'),
    
    
    # ============= URLs PARA POTREROS =============
    
    # Lista de potreros
    path('potreros/', views.PotreroListView.as_view(), name='potrero_list'),
    
    # Detalle de potrero
    path('potreros/<int:pk>/', views.PotreroDetailView.as_view(), name='potrero_detail'),
    
    # Crear potrero
    path('potreros/crear/', views.PotreroCreateView.as_view(), name='potrero_create'),
    
    # Editar potrero
    path('potreros/<int:pk>/editar/', views.PotreroUpdateView.as_view(), name='potrero_edit'),
    
    # Eliminar potrero
    path('potreros/<int:pk>/eliminar/', views.PotreroDeleteView.as_view(), name='potrero_delete'),
    
    
    # ============= URLs AJAX/API =============
    
    # Obtener potreros por finca (AJAX)
    path('ajax/potreros-por-finca/', views.potrero_by_finca_ajax, name='potrero_by_finca_ajax'),
    
    # Estadísticas de finca (AJAX)
    path('ajax/finca/<int:finca_id>/estadisticas/', views.finca_estadisticas_ajax, name='finca_estadisticas_ajax'),
]

# URLs alternativas más específicas si necesitas organizar mejor tu aplicación
app_name = 'ganaderia'  # Namespace para las URLs

# Si prefieres un enfoque más organizado, puedes usar:
"""
urlpatterns = [
    # Fincas
    path('', views.FincaListView.as_view(), name='finca_list'),  # Página principal
    path('finca/', include([
        path('', views.FincaListView.as_view(), name='finca_list'),
        path('nueva/', views.FincaCreateView.as_view(), name='finca_create'),
        path('<int:pk>/', views.FincaDetailView.as_view(), name='finca_detail'),
        path('<int:pk>/editar/', views.FincaUpdateView.as_view(), name='finca_edit'),
        path('<int:pk>/eliminar/', views.FincaDeleteView.as_view(), name='finca_delete'),
    ])),
    
    # Potreros
    path('potrero/', include([
        path('', views.PotreroListView.as_view(), name='potrero_list'),
        path('nuevo/', views.PotreroCreateView.as_view(), name='potrero_create'),
        path('<int:pk>/', views.PotreroDetailView.as_view(), name='potrero_detail'),
        path('<int:pk>/editar/', views.PotreroUpdateView.as_view(), name='potrero_edit'),
        path('<int:pk>/eliminar/', views.PotreroDeleteView.as_view(), name='potrero_delete'),
    ])),
    
    # AJAX
    path('ajax/', include([
        path('potreros-por-finca/', views.potrero_by_finca_ajax, name='potrero_by_finca_ajax'),
        path('finca/<int:finca_id>/estadisticas/', views.finca_estadisticas_ajax, name='finca_estadisticas_ajax'),
    ])),
]
"""

 