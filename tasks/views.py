from django.shortcuts import render, redirect, get_object_or_404
from http.client import HTTPResponse
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.db import IntegrityError
from django.contrib import messages
from django.urls import reverse
from.models import *
from .forms import FincaForm
from django.db.models import Count, Sum
from decimal import Decimal, ROUND_HALF_UP
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
    return render(request, 'profile.html', {
        'user': request.user
    })


def PanelInformativo(request, ):
    total_animales = Animal.objects.count()
    
    produccion_total = Registroproduccion.objects.aggregate(total=Sum('cantidad'))['total'] or 0

   
    
    nacimientos_mes = Registroreproduccion.objects.filter(
        tipoevento='Parto',
    ).count()

    context = {
        'total_animales': total_animales,
        'produccion_total': produccion_total,
        'nacimientos_mes': nacimientos_mes,
        'usuario':Usuario
    }
    return render(request, 'task.html', context)

def usuario_login(request, usuario_id):
    usuario = get_object_or_404(Usuario, idusuario =usuario_id)
    

# Listar fincas
def listar_fincas(request):
    fincas = Finca.objects.all()
    return render(request, 'fincas/listar.html', {'fincas': fincas})

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
