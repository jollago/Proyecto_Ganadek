from django.shortcuts import render, redirect, get_object_or_404
from http.client import HTTPResponse
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.db import IntegrityError
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from.models import *
from .forms import FincaForm, PotreroForm,PotreroCreateForm,PotreroQuickForm,PotreroEditForm
from django.db.models import Count, Sum, Q
from decimal import Decimal, ROUND_HALF_UP
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.



# views.py

@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Tu contraseña ha sido cambiada exitosamente.')
            return redirect('profile')  # Redirige al perfil
        else:
            messages.error(request, 'Por favor corrige los errores abajo.')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'password_change.html', {'form': form})



def signup(request):
    
    if request.method == 'GET':
         return render( request,'signup.html',{
        'form':UserCreationForm
    })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], 
                password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('PanelInformativo')
            except IntegrityError: 
                return render(request, 'signup.html',{
                    'form':UserCreationForm,
                    "error":'Usuario ya existente'
                })
             #registrar usuario
        return render(request, 'signup.html',{
                    'form':UserCreationForm,
                    "error":'La contraseña no coincide'
                })
  
        
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        
        return render (request, 'signin.html',{
            'form': AuthenticationForm
        })
    else:
        user= authenticate(request, username=request.POST['username'],
            password=request.POST['password'])      
        if user is None:
            return render (request, 'signin.html',{
            'form': AuthenticationForm,
            'error': 'Usuario o Contraseña incorrecta'
        })
        else:
            login(request,user)
            return redirect('PanelInformativo')
    
def home (request):
    return render(request, 'home.html',)

def profile(request):
    user = request.user
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.email = request.POST.get('email', '')
        user.save()
        if user:
          # Si el usuario se actualizó correctamente, muestra un mensaje de éxito
                messages.success(request, 'Perfil actualizado exitosamente.')
        else:
            # Si hubo un error al actualizar el usuario, muestra un mensaje de error
            messages.error(request, 'Error al actualizar el perfil. Por favor, inténtalo de nuevo.')
        return redirect('profile')  # Redirige para evitar doble envío
    # Si el método no es POST, simplemente renderiza el perfil 
    return render(request, 'profile.html', {
        'user': request.user
    })



def PanelInformativo(request, ):
    total_animales = Animal.objects.count()
    
    produccion_total = Registroproduccion.objects.aggregate(total=Sum('cantidad'))['total'] or 0

    empleados_activos = Empleado.objects.filter(estado='Activo').count()
    
    nacimientos_mes = Registroreproduccion.objects.filter(
        tipoevento='Parto',
    ).count()

    context = {
        'total_animales': total_animales,
        'produccion_total': produccion_total,
        'nacimientos_mes': nacimientos_mes,
        'empleados_activos': Empleado.objects.filter(estado='Activo').count(),        
        'usuario_nombre': request.user.username if request.user.is_authenticated else 'Usuario',
    }
    return render(request, 'task.html', context)

def usuario_login(request, usuario_id):
    usuario = get_object_or_404(Usuario, idusuario =usuario_id)
    

# Listar fincas
def listar_fincas(request):
    fincas = Finca.objects.all()
    return render(request, 'finca.html', {'fincas': fincas})

# Crear finca
def crear_finca(request):
    if request.method == 'POST':
        form = FincaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_fincas')
    else:
        form = FincaForm()
    return render(request, 'fincas/formulario.html', {'form': form, 'form_title': 'Nueva Finca'})

# Editar finca
def editar_finca(request, finca_id):
    finca = get_object_or_404(Finca, idfinca=finca_id)
    if request.method == 'POST':
        form = FincaForm(request.POST, instance=finca)
        if form.is_valid():
            form.save()
            return redirect('listar_fincas')
    else:
        form = FincaForm(instance=finca)
    return render(request, 'fincas/formulario.html', {'form': form, 'form_title': 'Editar Finca'})

# Eliminar finca
def eliminar_finca(request, finca_id):
    finca = get_object_or_404(Finca, idfinca=finca_id)
    if request.method == 'POST':
        finca.delete()
        return redirect('listar_fincas')
    return render(request, 'fincas/confirmar_eliminar.html', {'finca': finca})




# ============= VISTAS PARA FINCA =============

class FincaListView(LoginRequiredMixin, ListView):
    model = Finca
    template_name = 'finca_list.html'
    context_object_name = 'fincas'
    paginate_by = 12
    
    def get_queryset(self):
        
        queryset = Finca.objects.all().prefetch_related('potreros')
        
        search = self.request.GET.get('search', '').strip()

        if search:
            queryset = queryset.filter(nombre__icontains=search,ubicacion__icontains=search)

        
        # Filtro por estado
        estado = self.request.GET.get('estado')
        if estado:
            queryset = queryset.filter(estado=estado)
        
        return queryset.order_by('-fecha_creacion')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agregar estadísticas generales si es necesario
        context['total_fincas'] = Finca.objects.count()
        context['fincas_activas'] = Finca.objects.filter(estado='activo').count()
        return context


class FincaDetailView(LoginRequiredMixin, DetailView):
    model = Finca
    template_name = 'finca_detail.html'
    context_object_name = 'finca'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        finca = self.get_object()
        
        # Agregar estadísticas de potreros
        context['total_potreros'] = finca.potreros.count()
        context['potreros_disponibles'] = finca.potreros.filter(estado='disponible').count()
        context['potreros_ocupados'] = finca.potreros.filter(estado='ocupado').count()
        context['area_total_potreros'] = sum(p.area for p in finca.potreros.all())
        
        # Agregar animales si el modelo existe
        if hasattr(finca, 'animales'):
            context['total_animales'] = finca.animales.count()
            context['animales_activos'] = finca.animales.filter(estado='activo').count()
        
        return context


class FincaCreateView(LoginRequiredMixin, CreateView):
    model = Finca
    form_class = FincaForm
    template_name = 'finca_create.html'
    success_url = reverse_lazy('finca_list')
    
    def form_valid(self, form):
        messages.success(self.request, f'Finca "{form.instance.nombre}" creada exitosamente.')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Nueva Finca'
        context['submit_text'] = 'Crear Finca'
        return context


class FincaUpdateView(LoginRequiredMixin, UpdateView):
    model = Finca
    form_class = FincaForm
    template_name = 'finca_form.html'
    success_url = reverse_lazy('finca_list')
    
    def form_valid(self, form):
        messages.success(self.request, f'Finca "{form.instance.nombre}" actualizada exitosamente.')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Editar Finca: {self.object.nombre}'
        context['submit_text'] = 'Actualizar Finca'
        return context


class FincaDeleteView(LoginRequiredMixin, DeleteView):
    model = Finca
    template_name = 'finca_confirm_delete.html'
    success_url = reverse_lazy('finca_list')
    
    def delete(self, request, *args, **kwargs):
        finca = self.get_object()
        messages.success(request, f'Finca "{finca.nombre}" eliminada exitosamente.')
        return super().delete(request, *args, **kwargs)


# ============= VISTAS PARA POTRERO =============

class PotreroListView(LoginRequiredMixin, ListView):
    model = Potrero
    template_name = 'potreros/potrero_list.html'
    context_object_name = 'potreros'
    paginate_by = 12
    
    def get_queryset(self):
        queryset = Potrero.objects.all().select_related('finca')
        
        # Filtro por búsqueda
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(nombre__icontains=search) |
                Q(codigo__icontains=search) |
                Q(finca__nombre__icontains=search)
            )
        
        # Filtro por finca
        finca_id = self.request.GET.get('finca')
        if finca_id:
            queryset = queryset.filter(finca_id=finca_id)
        
        # Filtro por estado
        estado = self.request.GET.get('estado')
        if estado:
            queryset = queryset.filter(estado=estado)
        
        # Filtro por tipo de pasto
        tipo_pasto = self.request.GET.get('tipo_pasto')
        if tipo_pasto:
            queryset = queryset.filter(tipo_pasto=tipo_pasto)
        
        return queryset.order_by('-fecha_creacion')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fincas'] = Finca.objects.filter(estado='activo').order_by('nombre')
        context['total_potreros'] = Potrero.objects.count()
        context['potreros_disponibles'] = Potrero.objects.filter(estado='disponible').count()
        context['potreros_ocupados'] = Potrero.objects.filter(estado='ocupado').count()
        return context


class PotreroDetailView(LoginRequiredMixin, DetailView):
    model = Potrero
    template_name = 'potreros/potrero_detail.html'
    context_object_name = 'potrero'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        potrero = self.get_object()
        
        # Agregar animales en el potrero si el modelo existe
        if hasattr(potrero, 'animales'):
            context['animales_en_potrero'] = potrero.animales.filter(estado='activo')
            context['total_animales'] = potrero.animales.filter(estado='activo').count()
        
        # Calcular utilización del potrero
        if potrero.capacidad_animales and hasattr(potrero, 'animales'):
            animales_actuales = potrero.animales.filter(estado='activo').count()
            context['porcentaje_ocupacion'] = (animales_actuales / potrero.capacidad_animales) * 100
        
        return context


class PotreroCreateView(LoginRequiredMixin, CreateView):
    model = Potrero
    form_class = PotreroForm
    template_name = 'potreros/potrero_form.html'
    success_url = reverse_lazy('potrero_list')
    
    def get_initial(self):
        initial = super().get_initial()
        # Si se pasa finca como parámetro, pre-seleccionarla
        finca_id = self.request.GET.get('finca')
        if finca_id:
            initial['finca'] = finca_id
        return initial
    
    def form_valid(self, form):
        messages.success(self.request, f'Potrero "{form.instance.nombre}" creado exitosamente.')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Nuevo Potrero'
        context['submit_text'] = 'Crear Potrero'
        return context


class PotreroUpdateView(LoginRequiredMixin, UpdateView):
    model = Potrero
    form_class = PotreroForm
    template_name = 'potreros/potrero_form.html'
    success_url = reverse_lazy('potrero_list')
    
    def form_valid(self, form):
        messages.success(self.request, f'Potrero "{form.instance.nombre}" actualizado exitosamente.')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Editar Potrero: {self.object.nombre}'
        context['submit_text'] = 'Actualizar Potrero'
        return context


class PotreroDeleteView(LoginRequiredMixin, DeleteView):
    model = Potrero
    template_name = 'potreros/potrero_confirm_delete.html'
    success_url = reverse_lazy('potrero_list')
    
    def delete(self, request, *args, **kwargs):
        potrero = self.get_object()
        messages.success(request, f'Potrero "{potrero.nombre}" eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)


# ============= VISTAS AJAX/API =============

def potrero_by_finca_ajax(request):
    """Vista AJAX para obtener potreros por finca"""
    finca_id = request.GET.get('finca_id')
    potreros = Potrero.objects.filter(finca_id=finca_id, estado='disponible').values('id', 'nombre')
    return JsonResponse(list(potreros), safe=False)


def finca_estadisticas_ajax(request, finca_id):
    """Vista AJAX para obtener estadísticas de una finca"""
    finca = get_object_or_404(Finca, id=finca_id)
    
    data = {
        'total_potreros': finca.potreros.count(),
        'potreros_disponibles': finca.potreros.filter(estado='disponible').count(),
        'potreros_ocupados': finca.potreros.filter(estado='ocupado').count(),
        'area_total': float(finca.area_total),
        'area_potreros': sum(float(p.area) for p in finca.potreros.all()),
    }
    
    # Agregar datos de animales si existe el modelo
    if hasattr(finca, 'animales'):
        data['total_animales'] = finca.animales.filter(estado='activo').count()
    
    return JsonResponse(data)