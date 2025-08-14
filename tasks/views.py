from django.shortcuts import render, redirect, get_object_or_404
from http.client import HTTPResponse
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt 
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.db import IntegrityError
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from.models import *
from .forms import CustomUserCreationForm, FincaForm, UnidadProductivaForm
from django.db.models import Count, Sum, Q
from decimal import Decimal, ROUND_HALF_UP
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.timezone import now
from django import forms

# ============= VISTAS PARA GESTION DE USUARIOS =============
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
                user = User.objects.get(username =request.POST['username'])
                user.last_login = now()
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
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])

        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o Contraseña incorrecta'
            })
        if user.is_active == False:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Tu cuenta ha sido desactivada. Contacta al administrador.'
            })
        else:
            login(request, user)  
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect('PanelInformativo')
    
def home (request):
    return render(request, 'home.html',)

def profile(request):
    user = request.user
    if request.method == 'POST':
        nuevo_username = request.POST.get('username', '').strip()
        nuevo_first_name = request.POST.get('first_name', '').strip()
        nuevo_last_name = request.POST.get('last_name', '').strip()
        nuevo_email = request.POST.get('email', '').strip()

        if User.objects.exclude(pk=user.pk).filter(username=nuevo_username).exists():
            messages.error(request, 'El nombre de usuario ya está en uso por otro usuario.')
            return redirect('profile')

        try:
            user.username = nuevo_username
            user.first_name = nuevo_first_name
            user.last_name = nuevo_last_name
            user.email = nuevo_email
            user.save()
            messages.success(request, 'Perfil actualizado exitosamente.')
        except IntegrityError:
            messages.error(request, 'Ocurrió un error al actualizar el perfil. Inténtalo nuevamente.')
        
        return redirect('profile')

    return render(request, 'profile.html', { 
        'user': user,
        'ultimo_acceso': request.user.last_login 
        
    })


# Form personalizado para crear/editar usuarios
class CustomUserForm(forms.ModelForm):
    
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(),
        required=False,
        help_text='Mínimo 8 caracteres'
    )
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(),
        required=False
    )
    role = forms.ChoiceField(
        choices=[
            ('user', 'Usuario'),
            ('staff', 'Staff'),
            ('admin', 'Administrador')
        ],
        required=False,
        initial='user'
    )
    status = forms.ChoiceField(
        choices=[
            ('active', 'Activo'),
            ('inactive', 'Inactivo')
        ],
        required=False,
        initial='active'
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        self.is_editing = kwargs.pop('is_editing', False)
        super().__init__(*args, **kwargs)
        
        # Si estamos editando, la contraseña no es requerida
        if not self.is_editing:
            self.fields['password1'].required = True
            self.fields['password2'].required = True

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if not self.is_editing and password1 and password2:
            if password1 != password2:
                raise forms.ValidationError("Las contraseñas no coinciden")
            if len(password1) < 8:
                raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres")
        
        return password2

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if self.instance.pk:
            # Si estamos editando, excluir el usuario actual de la verificación
            if User.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError("Este nombre de usuario ya existe")
        else:
            # Si estamos creando, verificar que no exista
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError("Este nombre de usuario ya existe")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if self.instance.pk:
            # Si estamos editando, excluir el usuario actual de la verificación
            if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError("Este email ya está registrado")
        else:
            # Si estamos creando, verificar que no exista
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("Este email ya está registrado")
        return 
    
    
    

def gestion_usuarios(request):
    # Verificar que el usuario tenga permisos de administrador
    if not request.user.is_staff:
        messages.error(request, 'No tienes permisos para acceder a esta página')
        return redirect('PanelInformativo')  # o la página que corresponda

    if request.method == 'POST':
        action = request.POST.get('action')
        user_id = request.POST.get('user_id')

        try:
            if action == 'delete':
                if user_id == str(request.user.id):
                    messages.error(request, 'No puedes eliminar tu propio usuario')
                else:
                    user = get_object_or_404(User, id=user_id)
                    username = user.username
                    user.delete()
                    messages.success(request, f'Usuario "{username}" eliminado correctamente')

            elif action == 'toggle_status':
                if user_id == str(request.user.id):
                    messages.error(request, 'No puedes cambiar tu propio estado')
                else:
                    user = get_object_or_404(User, id=user_id)
                    user.is_active = not user.is_active
                    user.save()
                    status = 'activado' if user.is_active else 'desactivado'
                    messages.success(request, f'Usuario "{user.username}" {status} correctamente')
            

            elif action == 'create':
                
                form = CustomUserForm(request.POST, is_editing=False)
                if form.is_valid():
                    print("Formulario válido")
                    print(form.cleaned_data)


                    user = form.save(commit=False)
                    
                    # Establecer contraseña
                    password = form.cleaned_data.get('password1')
                    if password:
                        user.set_password(password)
                    
                    # Establecer rol
                    role = form.cleaned_data.get('role', 'user')
                    if role == 'admin':
                        user.is_staff = True
                        user.is_superuser = True
                    elif role == 'staff':
                        user.is_staff = True
                        user.is_superuser = False
                    else:
                        user.is_staff = False
                        user.is_superuser = False
                    
                    # Establecer estado
                    status = form.cleaned_data.get('status', 'active')
                    user.is_active = (status == 'active')
                    
                    user.save()
                    messages.success(request, f'Usuario "{user.username}" creado correctamente')
                else:

                    # Si hay errores, mostrar el modal con los errores
                    usuarios = User.objects.all().order_by('username')
                    return render(request, 'gestion_usuario.html', {
                        'usuarios': usuarios,
                        'form': form,
                        'show_modal': True,
                        'error': 'Por favor corrige los errores en el formulario'
                    })

            elif action == 'edit':
                user = get_object_or_404(User, id=user_id)
                form = CustomUserForm(request.POST, instance=user, is_editing=True)
                if form.is_valid():
                    user = form.save(commit=False)
                    
                    # Actualizar rol
                    role = request.POST.get('role', 'user')
                    if role == 'admin':
                        user.is_staff = True
                        user.is_superuser = True
                    elif role == 'staff':
                        user.is_staff = True
                        user.is_superuser = False
                    else:
                        user.is_staff = False
                        user.is_superuser = False
                    
                    # Actualizar estado
                    status = request.POST.get('status', 'active')
                    user.is_active = (status == 'active')
                    
                    # Actualizar contraseña solo si se proporcionó una nueva
                    password = form.cleaned_data.get('password1')
                    if password:
                        user.set_password(password)
                    
                    user.save()
                    messages.success(request, f'Usuario "{user.username}" actualizado correctamente')
                else:
                    # Si hay errores, mostrar el modal con los errores
                    usuarios = User.objects.all().order_by('username')
                    return render(request, 'gestion_usuario.html', {
                        'usuarios': usuarios,
                        'form': form,
                        'show_modal': True,
                        'error': 'Por favor corrige los errores en el formulario'
                    })

        except Exception as e:
            messages.error(request, f'Error al procesar la acción: {str(e)}')

        return redirect('gestion_usuarios')

    # GET request - mostrar la página
    usuarios = User.objects.all().order_by('username')
    form = CustomUserForm()
    
    return render(request, 'gestion_usuario.html', {
        'usuarios': usuarios,
        'form': form,
        'show_modal': False
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
    


# ============= VISTAS PARA FINCA =============

class FincaListView(LoginRequiredMixin, ListView):
    model = Finca
    template_name = 'finca_list.html'
    context_object_name = 'fincas'
    paginate_by = 12
    
    def get_queryset(self):
        queryset = Finca.objects.all().prefetch_related('unidades_productivas')
        
        # Filtro por búsqueda
        if 'search' in self.request.GET:
            search = self.request.GET['search'].strip()
            if search:
                queryset = queryset.filter(Q(nombre__icontains=search) | Q(ubicacion__icontains=search))
        else:
            # Si no hay búsqueda, mostrar todas las fincas
            queryset = Finca.objects.all().prefetch_related('unidades_productivas')  # También acá

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
        Propietario = finca.cedulapropietario # Asumiendo que cedulapropietario es una relación con el modelo Propietario
        context['propietario'] = Propietario
        context['cedulapropietario'] = Propietario.cedulapropietario if Propietario else 'No disponible'
        context['tipo_documento'] = Propietario.tipodocumento if Propietario else 'No disponible'
        context['Pnombre'] = Propietario.nombre if Propietario else 'No disponible'
        context['Ptelefono'] = Propietario.telefono if Propietario else 'No disponible'
        context['Pemail'] = Propietario.correo if Propietario else 'No disponible'
        unidades = finca.unidades_productivas.all()

        context['total_u_productiva'] = unidades.count()
        context['u_productiva_disponibles'] = unidades.filter(estado='disponible').count()
        context['u_productiva_ocupados'] = unidades.filter(estado='ocupado').count()
        context['area_total_u_productiva'] = sum(p.area for p in unidades)

        return context
    
class FincaCreateView(LoginRequiredMixin, CreateView):
    model = Finca
    form_class = FincaForm
    template_name = 'finca_create.html'
    success_url = reverse_lazy('finca_list')  # Asegúrate que esta URL exista
    
    def form_invalid(self, form):
        print("Errores del formulario:", form.errors)
        return super().form_invalid(form)
    def form_valid(self, form):
        print("Formulario válido. Guardando...")
        return super().form_valid(form)

class FincaUpdateView(LoginRequiredMixin, UpdateView):
    model = Finca
    form_class = FincaForm
    template_name = 'finca_edit.html'
    success_url = reverse_lazy('finca_list')
    
    def form_valid(self, form):
        messages.success(self.request, f'Finca "{form.instance.nombre}" actualizada exitosamente.')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Editar Finca: {self.object.nombre}'
        context['submit_text'] = 'Actualizar Finca'
        return context

class FincaDeleteView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        finca_id = kwargs.get('pk')
        finca = get_object_or_404(Finca, pk=finca_id)
        finca.delete()
        messages.success(request, f'Finca "{finca.nombre}" eliminada exitosamente.')
        return redirect('finca_list')

# ============= VISTAS PARA UNIDAD PRODUCTIVA =============

class UnidadProductivaListView(LoginRequiredMixin, ListView):
    model = UnidadProductiva
    template_name = 'unidad_productiva_list.html'
    context_object_name = 'unidades_productivas'
    paginate_by = 12

    def get_queryset(self):
        queryset = UnidadProductiva.objects.all().select_related('idfinca')
        
        # Filtro por búsqueda
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(nombre__icontains=search) |
                Q(finca__nombre__icontains=search)
            )

        # Filtro por finca
        finca_id = self.request.GET.get('idfinca')
        if finca_id:
            queryset = queryset.filter(finca_id=finca_id)

        # Filtro por estado
        estado = self.request.GET.get('estado')
        if estado:
            queryset = queryset.filter(estado=estado)

        # Filtro por tipo de unidad (si aplica)
        tipo_unidad = self.request.GET.get('tipo_unidad')
        if tipo_unidad:
            queryset = queryset.filter(tipo_unidad=tipo_unidad)
        


        return queryset.order_by('-idfinca')
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fincas'] = Finca.objects.filter(estado='activo').order_by('nombre')
        context['total_unidades'] = UnidadProductiva.objects.count()
        context['unidades_disponibles'] = UnidadProductiva.objects.filter(estado='disponible').count()
        context['unidades_ocupadas'] = UnidadProductiva.objects.filter(estado='ocupado').count()
        return context


class UnidadProductivaDetailView(LoginRequiredMixin, DetailView):
    model = UnidadProductiva
    template_name = 'unidad_productiva_detail.html'
    context_object_name = 'unidad_productiva'

    def unidad_productiva_detail(request, pk):
        unidad_productiva = get_object_or_404(UnidadProductiva, pk=pk)
        return render(request, 'unidad_productiva_detail.html', {
            'unidad_productiva': unidad_productiva
        })


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        unidad = self.get_object()

        # Agregar animales en la unidad si el modelo existe
        if hasattr(unidad, 'animales'):
            context['animales_en_unidad'] = unidad.animales.filter(estado='activo')
            context['total_animales'] = unidad.animales.filter(estado='activo').count()

        # Calcular utilización de la unidad
        if unidad.capacidad_maxima and hasattr(unidad, 'animales'):
            animales_actuales = unidad.animales.filter(estado='activo').count()
            context['porcentaje_ocupacion'] = (animales_actuales / unidad.capacidad_maxima) * 100

        return context
  
class UnidadProductivaCreateView(LoginRequiredMixin, CreateView):
    model = UnidadProductiva
    form_class = UnidadProductivaForm
    template_name = 'unidad_productiva_create.html'
    success_url = reverse_lazy('UnidadProductiva_list')

    def get_initial(self):
        initial = super().get_initial()
        finca_id = self.request.GET.get('idfinca')
        if finca_id:
            initial['finca'] = finca_id
        return initial

    def form_valid(self, form):
        messages.success(self.request, f'Unidad Productiva "{form.instance.nombre}" creada exitosamente.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Nueva Unidad Productiva'
        context['submit_text'] = 'Crear Unidad Productiva'
        return context

class UnidadProductivaUpdateView(LoginRequiredMixin, UpdateView):
    model = UnidadProductiva
    form_class = UnidadProductivaForm
    template_name = 'unidad_productiva_edit.html'
    success_url = reverse_lazy('UnidadProductiva_list')

    def form_valid(self, form):
        messages.success(self.request, f'Unidad Productiva "{form.instance.nombre}" actualizada exitosamente.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Editar Unidad Productiva: {self.object.nombre}'
        context['submit_text'] = 'Actualizar Unidad Productiva'
        return context

class UnidadProductivaDeleteView(LoginRequiredMixin, DeleteView):
    model = UnidadProductiva
    success_url = reverse_lazy('UnidadProductiva_list')

    def delete(self, request, *args, **kwargs):
        unidadp = kwargs.get('pk')
        unidadProductiva = get_object_or_404(UnidadProductiva, pk=unidadp)
        unidadProductiva.delete()
        unidad = self.get_object()
        messages.success(request, f'Unidad Productiva "{unidad.nombre}" eliminada exitosamente.')
        return super().delete(request, *args, **kwargs)
    

    
# ============= VISTAS PARA ANIMAL =============

class AnimalListView(LoginRequiredMixin, ListView):
    model = Animal
    template_name = 'animal_list.html'
    context_object_name = 'animales'
    paginate_by = 12
            
    def get_queryset(self):
        queryset = Animal.objects.select_related('idunidad', 'idmadre', 'idpadre')
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(especie__icontains=search) |
                Q(raza__icontains=search) |
                Q(sexo__icontains=search) |
                Q(idunidad__nombre__icontains=search)
            )
        estado = self.request.GET.get('estado')
        if estado:
            queryset = queryset.filter(estado=estado)
        return queryset.order_by('-idanimal')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_animales'] = Animal.objects.count()
        context['animales_activos'] = Animal.objects.filter(estado='activo').count()
        context['animales_inactivos'] = Animal.objects.exclude(estado='activo').count()
        return context

class AnimalDetailView(LoginRequiredMixin, DetailView):
    model = Animal
    template_name = 'animal_detail.html'
    context_object_name = 'animal'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        animal = self.get_object()
        context['unidad'] = animal.idunidad
        context['madre'] = animal.idmadre
        context['padre'] = animal.idpadre
        return context
class AnimalCreateView(LoginRequiredMixin, CreateView):
    model = Animal
    fields = ['idunidad', 'especie', 'raza', 'sexo', 'peso', 'fechanacimiento', 'idmadre', 'idpadre', 'imagen', 'estado']
    template_name = 'animal_create.html'
    success_url = reverse_lazy('animal_list')

    def get_initial(self):
        initial = super().get_initial()
        unidad_id = self.request.GET.get('idunidad') or self.request.GET.get('UnidadProductiva')
        if unidad_id:
            initial['idunidad'] = unidad_id
        return initial


    def form_valid(self, form):
        messages.success(self.request, 'Animal creado exitosamente.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registrar Nuevo Animal'
        context['submit_text'] = 'Registrar Animal'
        return context

class AnimalUpdateView(LoginRequiredMixin, UpdateView):
    model = Animal
    fields = ['idunidad', 'especie', 'raza', 'sexo', 'peso', 'fechanacimiento', 'idmadre', 'idpadre', 'imagen', 'estado']
    template_name = 'animal_edit.html'
    success_url = reverse_lazy('animal_list')

    def form_valid(self, form):
        messages.success(self.request, f'Animal actualizado exitosamente.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Editar Animal: {self.object.idanimal}'
        context['submit_text'] = 'Actualizar Animal'
        return context

class AnimalDeleteView(LoginRequiredMixin, DeleteView):
    model = Animal
    template_name = 'animal_confirm_delete.html'
    success_url = reverse_lazy('animal_list')

    def delete(self, request, *args, **kwargs):
        animal = self.get_object()
        messages.success(request, f'Animal eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)