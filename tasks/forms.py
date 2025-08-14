
# forms.py
from django import forms
from decimal import Decimal
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from decimal import Decimal, InvalidOperation



class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(     choices=[
        ('none', 'Usuario'),
        ('staff', 'Staff'),
        ('admin', 'Superusuario'),
    ],widget=forms.Select(attrs={ 
        'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500 transition-all duration-200',
    
        }))
    status = forms.ChoiceField(choices=[
        ('active', 'Activo'),
        ('inactive', 'Inactivo')
    ],widget=forms.Select(attrs={
        'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500 transition-all duration-200',
    }))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'role', 'status']


    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        role = self.cleaned_data['role']
        if role == 'admin':
            user.is_staff = True
            user.is_superuser = True
        elif role == 'staff':
            user.is_staff = True
            user.is_superuser = False
        else:  # 'none'
            user.is_staff = False
            user.is_superuser = False
        # Asignación de estado
        user.is_active = self.cleaned_data['status'] == 'active'

        if commit:
            user.save()
        return user

class FincaForm(forms.ModelForm):
        
    fuenteagua = forms.ChoiceField(
        choices = [
            ('', 'Seleccionar fuente...'),
            ('Río', 'Río'),
            ('Quebrada', 'Quebrada'),
            ('Pozo', 'Pozo'),
            ('Lago', 'Lago'),
            ('Otro', 'Otro')
        ],
    widget=forms.Select(attrs={
        'class': 'form-control w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent transition duration-200',

    }))
    explotacion = forms.ChoiceField(
        choices=[
            ('', 'Seleccionar tipo...'),
            ('Ganadería', 'Ganadería'),
            ('Avicultura', 'Avicultura'),
            ('Porcicultura', 'Porcicultura'),
            ('Mixta', 'Mixta'),
            ('Otro', 'Otro')
        ],
    widget=forms.Select(attrs={
        'class': 'form-control w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent transition duration-200',
    }))
    estado = forms.ChoiceField(
        choices=[
            ('Activo', 'Activo'),
            ('Inactivo', 'Inactivo'),
        ],
    widget=forms.Select(attrs={
        'class': 'form-control w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent transition duration-200',
    }))
    latitud = forms.DecimalField(
        max_digits=15,
        decimal_places=10,
        widget=forms.NumberInput(attrs={
            'class': 'form-control w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent transition duration-200',
            'step': 'any',
            'placeholder': '-5.5884512345',
            'id': 'latitud',
            'lang': 'en',
            'inputmode': 'decimal'
        })
    )
    longitud = forms.DecimalField(
        max_digits=15,
        decimal_places=10,
        widget=forms.NumberInput(attrs={
            'class': 'form-control w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent transition duration-200',
            'step': 'any',
            'placeholder': '-72.9043160000',
            'id': 'longitud',
            'lang': 'en',
            'inputmode': 'decimal'
        })
    )
    hectareas = forms.FloatField(
        widget=forms.TextInput(attrs={
            'class': 'form-control w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent transition duration-200',
            'placeholder': 'Ej: 5.5',
        })
    )
    class Meta:
        model = Finca
        fields = [
            'cedulapropietario', 'nombre', 'ubicacion', 'latitud',
            'longitud', 'hectareas', 'fuenteagua', 'explotacion','estado'
        ]
       
        
        widgets = {
            'cedulapropietario': forms.TextInput(attrs={
                'class': 'form-control w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent transition duration-200',
             'placeholder': 'Cedula del propietario'
             }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent transition duration-200',
                'placeholder': 'Nombre de la finca'
            }),
            'ubicacion': forms.TextInput(attrs={
                'class': 'form-control w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent transition duration-200',
                'placeholder': 'Dirección o ubicación'
            }),
        }
        
        labels = {
            'cedulapropietario': 'Cédula del Propietario',
            'nombre': 'Nombre de la Finca',
            'ubicacion': 'Ubicación',
            'latitud': 'Latitud',
            'longitud': 'Longitud',
            'hectareas': 'Hectáreas',
            'fuenteagua': 'Fuente de Agua',
            'explotacion': 'Tipo de Explotación',
        }   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Hacer algunos campos requeridos
        self.fields['cedulapropietario'].required = True
        self.fields['nombre'].required = True
        self.fields['ubicacion'].required = True
        self.fields['latitud'].required = True
        self.fields['longitud'].required = True
        self.fields['hectareas'].required = True
        self.fields['fuenteagua'].required = True
        self.fields['explotacion'].required = True
        # Agregar clase CSS para el campo cedulapropietario
        self.fields['cedulapropietario'].empty_label = "Seleccione un propietario"
    def clean_latitud(self):
        latitud = self.cleaned_data.get('latitud')
        if latitud is not None:
            try:
                latitud = latitud
                if latitud < -90 or latitud > 90:
                    raise forms.ValidationError("La latitud debe estar entre -90 y 90 grados.")
            except ValueError:
                raise forms.ValidationError("Ingrese un valor numérico válido para la latitud.")
        return latitud
    def clean_longitud(self):
        longitud = self.cleaned_data.get('longitud')
        if longitud is not None:
            try:
                longitud = longitud
                if longitud < -180 or longitud > 180:
                    raise forms.ValidationError("La longitud debe estar entre -180 y 180 grados.")
            except ValueError:
                raise forms.ValidationError("Ingrese un valor numérico válido para la longitud.")
        return longitud
    def clean_hectareas(self):
        hectareas = self.cleaned_data.get('hectareas')
        if hectareas is not None:
            try:
                hectareas = hectareas
                if hectareas <= 0:
                    raise forms.ValidationError("El número de hectáreas debe ser mayor a 0.")
            except ValueError:
                raise forms.ValidationError("Ingrese un valor numérico válido para las hectáreas.")
        return hectareas
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        qs = Finca.objects.filter(nombre__iexact=nombre)
        if self.instance and self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("Ya existe una finca con este nombre.")
        return nombre
    def clean_ubicacion(self):
        ubicacion = self.cleaned_data.get('ubicacion')
        if ubicacion:
            qs = Finca.objects.filter(ubicacion=ubicacion)
            if self.instance and self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise forms.ValidationError("Ya existe una finca con esta ubicación.")
        return ubicacion

    def clean_cedulapropietario(self):
        cedulapropietario = self.cleaned_data.get('cedulapropietario')
        if cedulapropietario:
            qs = Finca.objects.filter(cedulapropietario=cedulapropietario)
            if self.instance and self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise forms.ValidationError("Ya existe una finca con esta cédula de propietario.")
        return cedulapropietario

    def clean_fuenteagua(self):
        fuenteagua = self.cleaned_data.get('fuenteagua')
        if fuenteagua:
            # Validación adicional de fuente de agua si es necesario
            return fuenteagua.strip()
        return fuenteagua
    def clean_explotacion(self):
        explotacion = self.cleaned_data.get('explotacion')
        if explotacion:
            # Validación adicional de tipo de explotación si es necesario
            return explotacion.strip()
        return explotacion
    def clean(self):
        cleaned_data = super().clean()
        latitud = cleaned_data.get('latitud')
        longitud = cleaned_data.get('longitud')
        
        if latitud is not None and longitud is not None:
            # Verificar que las coordenadas no sean nulas
            if latitud == 0 and longitud == 0:
                raise forms.ValidationError("Las coordenadas de ubicación no pueden ser nulas.")
        
        return cleaned_data
        # Validación adicional para el área total
    def clean_area_total(self):
        area_total = self.cleaned_data.get('hectareas')
        if area_total is not None and area_total <= 0:
            raise forms.ValidationError("El área total debe ser mayor a 0.")
        return area_total

class UnidadProductivaForm(forms.ModelForm):

    class Meta:
        model = UnidadProductiva
        fields = [
            'idunidad', 'idfinca', 'nombre', 'tipounidad', 'especie_destinada', 'area',
            'capacidad_maxima', 'descripcion', 'fuenteagua', 'tipopasto', 'tipoconstruccion',
            'sistemaventilacion', 'sistemaalimentacion', 'temperaturacontrolada', 'iluminacion', 'estado'
        ]
        widgets = {
            'idunidad': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald-500',
                'readonly': 'readonly'
            }),
            'idfinca': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald-500',
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald-500',
                'placeholder': 'Nombre de la Unidad Productiva',
            }),
            'tipounidad': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald-500',
            }),
            'especie_destinada': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald-500',
                'placeholder': 'Especie Destinada',
            }),
            'area': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald-500',
                'placeholder': 'Área (ha)',
                'step': '0.01',
                'min': '0'
            }),
            'capacidad_maxima': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald-500',
                'placeholder': 'Capacidad Máxima',
                'min': '0'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald-500',
                'placeholder': 'Descripción',
                'rows': 3
            }),
            'fuenteagua': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald-500',
                'placeholder': 'Fuente de agua',
            }),
            'tipopasto': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald-500',
                'placeholder': 'Tipo de pasto',
            }),
            'tipoconstruccion': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald-500',
                'placeholder': 'Tipo de Construcción',
            }),
            'sistemaventilacion': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald-500',
                'placeholder': 'Sistema de Ventilación',
            }),
            'sistemaalimentacion': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald-500',
                'placeholder': 'Sistema de Alimentación',
            }),
            'temperaturacontrolada': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald-500',
            }),
            'iluminacion': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald-500',
            }),
            'estado': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald-500',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Configurar queryset para fincas
        self.fields['idfinca'].queryset = Finca.objects.all().order_by('nombre')
        self.fields['idfinca'].empty_label = "Seleccione una finca"

        # Campos obligatorios
        required_fields = ['nombre', 'tipounidad', 'especie_destinada', 'area', 'estado']
        for field in required_fields:
            self.fields[field].required = True

        # Campos opcionales
        optional_fields = [
            'fuenteagua', 'tipopasto', 'tipoconstruccion', 'sistemaventilacion',
            'sistemaalimentacion', 'temperaturacontrolada', 'iluminacion'
        ]
        for field in optional_fields:
            self.fields[field].required = False

    def clean_area(self):
        area = self.cleaned_data.get('area')
        if area is not None:
            try:
                area = Decimal(area)
                if area <= 0:
                    raise forms.ValidationError("El área debe ser mayor a 0.")
            except InvalidOperation:
                raise forms.ValidationError("Ingrese un valor numérico válido para el área.")
        return area

    def clean_nombre(self):
        nombre = (self.cleaned_data.get('nombre') or '').strip()
        idfinca = self.cleaned_data.get('idfinca')
        qs = UnidadProductiva.objects.filter(nombre__iexact=nombre, idfinca=idfinca)
        if self.instance and self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("Ya existe una Unidad Productiva con este nombre en la finca seleccionada.")
        return nombre or None

    def clean_fuenteagua(self):
        return (self.cleaned_data.get('fuenteagua') or '').strip() or None

    def clean_tipopasto(self):
        return (self.cleaned_data.get('tipopasto') or '').strip() or None

    def clean(self):
        cleaned_data = super().clean()
        tipounidad = (cleaned_data.get('tipounidad') or '').casefold()

        # Para galpones y jaulas → limpiar campos de potrero
        if tipounidad in ['galpon', 'galpón', 'jaula']:
            cleaned_data['fuenteagua'] = None
            cleaned_data['tipopasto'] = None

        # Para potreros → limpiar campos de galpón/jaula
        elif tipounidad == 'potrero':
            cleaned_data['tipoconstruccion'] = None
            cleaned_data['sistemaventilacion'] = None
            cleaned_data['sistemaalimentacion'] = None
            cleaned_data['temperaturacontrolada'] = None
            cleaned_data['iluminacion'] = None

        return cleaned_data    
    
class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = [
            'idunidad', 'especie', 'raza', 'sexo', 'peso', 
            'fechanacimiento', 'idmadre', 'idpadre', 'imagen', 'estado'
        ]
        
        widgets = {
            'idunidad': forms.Select(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent transition duration-200',
            }),
            'especie': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent transition duration-200',
                'placeholder': 'Ej: Bovino',
            }),
            'raza': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent transition duration-200',
                'placeholder': 'Ej: Brahman',
            }), 'sexo': forms.Select(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent transition duration-200'
            }),
            'peso': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent transition duration-200',
                'placeholder': 'Peso en kg',
                'step': 'any',
                'min': '0',
            }),
            'fechanacimiento': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent transition duration-200',
            }),
            'idmadre': forms.Select(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent transition duration-200',
            }),
            'idpadre': forms.Select(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent transition duration-200',
            }),
            'imagen': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent transition duration-200',
                'placeholder': 'URL de la imagen (opcional)',
            }),
            'estado': forms.Select(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent transition duration-200',
            }),
        }
        
        labels = {
            'idunidad': 'Unidad Productiva',
            'especie': 'Especie',
            'raza': 'Raza',
            'sexo': 'Sexo',
            'peso': 'Peso (kg)',
            'fechanacimiento': 'Fecha de Nacimiento',
            'idmadre': 'Madre',
            'idpadre': 'Padre',
            'imagen': 'Imagen (URL)',
            'estado': 'Estado',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Configurar queryset para unidades productivas
        self.fields['idunidad'].queryset = UnidadProductiva.objects.all().order_by('nombre')
        self.fields['idunidad'].empty_label = "Seleccione una unidad productiva"
        
        # Configurar queryset para madre y padre (solo hembras y machos respectivamente)
        try:
            self.fields['idmadre'].queryset = Animal.objects.filter(sexo='Hembra').order_by('idanimal')
            self.fields['idmadre'].empty_label = "Seleccione la madre (opcional)"
            
            self.fields['idpadre'].queryset = Animal.objects.filter(sexo='Macho').order_by('idanimal')
            self.fields['idpadre'].empty_label = "Seleccione el padre (opcional)"
        except:
            # En caso de que no existan animales aún
            self.fields['idmadre'].queryset = Animal.objects.none()
            self.fields['idpadre'].queryset = Animal.objects.none()
        
        # Campos requeridos
        self.fields['idunidad'].required = True
        self.fields['peso'].required = True
        self.fields['fechanacimiento'].required = True
        self.fields['estado'].required = True
        self.fields['especie'].required = True
        self.fields['sexo'].required = True
        
        # Campos opcionales
        optional_fields = ['idmadre', 'idpadre', 'imagen']
        for field in optional_fields:
            self.fields[field].required = False
        
        # Estado por defecto
        self.fields['estado'].initial = 'Vivo'

    def clean_peso(self):
        peso = self.cleaned_data.get('peso')
        if peso is not None and peso <= 0:
            raise forms.ValidationError("El peso debe ser mayor a 0.")
        return peso

    def clean_especie(self):
        especie = self.cleaned_data.get('especie')
        if especie:
            return especie.strip().title()  # Capitalizar primera letra
        return especie

    def clean_raza(self):
        raza = self.cleaned_data.get('raza')
        if raza:
            return raza.strip().title()  # Capitalizar primera letra
        return raza

    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen')
        if imagen:
            # Validación básica de URL
            if not (imagen.startswith('http://') or imagen.startswith('https://')):
                raise forms.ValidationError("La imagen debe ser una URL válida que comience con http:// o https://")
        return imagen

    def clean(self):
        cleaned_data = super().clean()
        idmadre = cleaned_data.get('idmadre')
        idpadre = cleaned_data.get('idpadre')
        
        # Validar que madre y padre no sean el mismo animal
        if idmadre and idpadre and idmadre == idpadre:
            raise forms.ValidationError("La madre y el padre no pueden ser el mismo animal.")
        
        return cleaned_data
    
    
    