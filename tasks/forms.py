# forms.py
from django import forms
from .models import *

class FincaForm(forms.ModelForm):
    class Meta:
        model = Finca
        fields = [
            'cedulapropietario', 'nombre', 'ubicacion', 'latitud',
            'longitud', 'hectareas', 'fuenteagua', 'explotacion'
        ]
        widgets = {
            'cedulapropietario': forms.Select(attrs={
                'class': 'form-control'
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la finca'
            }),
            'ubicacion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Dirección o ubicación'
            }),
            'latitud': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'longitud': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'hectareas': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0'
            }),
            'fuenteagua': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'explotacion': forms.TextInput(attrs={
                'class': 'form-control'
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
                latitud = float(latitud)
                if latitud < -90 or latitud > 90:
                    raise forms.ValidationError("La latitud debe estar entre -90 y 90 grados.")
            except ValueError:
                raise forms.ValidationError("Ingrese un valor numérico válido para la latitud.")
        return latitud
    def clean_longitud(self):
        longitud = self.cleaned_data.get('longitud')
        if longitud is not None:
            try:
                longitud = float(longitud)
                if longitud < -180 or longitud > 180:
                    raise forms.ValidationError("La longitud debe estar entre -180 y 180 grados.")
            except ValueError:
                raise forms.ValidationError("Ingrese un valor numérico válido para la longitud.")
        return longitud
    def clean_hectareas(self):
        hectareas = self.cleaned_data.get('hectareas')
        if hectareas is not None:
            try:
                hectareas = float(hectareas)
                if hectareas <= 0:
                    raise forms.ValidationError("El número de hectáreas debe ser mayor a 0.")
            except ValueError:
                raise forms.ValidationError("Ingrese un valor numérico válido para las hectáreas.")
        return hectareas
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if nombre:
            # Verificar que el nombre sea único
            qs = Finca.objects.filter(nombre=nombre)
            if self.instance:
                qs = qs.exclude(id=self.instance.id)
            if qs.exists():
                raise forms.ValidationError("Ya existe una finca con este nombre.")
        return nombre
    def clean_ubicacion(self):
        ubicacion = self.cleaned_data.get('ubicacion')
        if ubicacion:
            # Verificar que la ubicación sea única
            qs = Finca.objects.filter(ubicacion=ubicacion)
            if self.instance:
                qs = qs.exclude(id=self.instance.id)
            if qs.exists():
                raise forms.ValidationError("Ya existe una finca con esta ubicación.")
        return ubicacion
    def clean_cedulapropietario(self):
        cedulapropietario = self.cleaned_data.get('cedulapropietario')
        if cedulapropietario:
            # Verificar que la cédula del propietario sea única
            qs = Finca.objects.filter(cedulapropietario=cedulapropietario)
            if self.instance:
                qs = qs.exclude(id=self.instance.id)
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
        

class PotreroForm(forms.ModelForm):
    class Meta:
        model = Potrero
        fields = ['idfinca', 'nombre', 'area', 'fuenteagua', 'tipopasto']
        widgets = {
            'idfinca': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald-500',
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald-500',
                'placeholder': 'Nombre del potrero',
            }),
            'area': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald-500',
                'placeholder': 'Área (ha)',
                'step': '0.01',
                'min': '0'
            }),
            'fuenteagua': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald-500',
                'placeholder': 'Fuente de agua',
            }),
            'tipopasto': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald-500',
                'placeholder': 'Tipo de pasto',
            }),
        }
        labels = {
            'idfinca': 'Finca',
            'nombre': 'Nombre',
            'area': 'Área (ha)',
            'fuenteagua': 'Fuente de Agua',
            'tipopasto': 'Tipo de Pasto',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['idfinca'].queryset = Finca.objects.all().order_by('nombre')
        self.fields['nombre'].required = True
        self.fields['area'].required = True

# Formulario simplificado para crear potrero desde la página de finca
class PotreroQuickForm(forms.ModelForm):
    class Meta:
        model = Potrero
        fields = ['nombre', 'area', 'fuenteagua', 'tipopasto']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-green-500',
                'placeholder': 'Nombre del potrero'
            }),
            'area': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-green-500',
                'placeholder': 'Área (ha)',
                'step': '0.01',
                'min': '0'
            }),
            'fuenteagua': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-green-500',
                'placeholder': 'Fuente de agua'
            }),
            'tipopasto': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-green-500',
                'placeholder': 'Tipo de pasto'
            }),
        }

    def __init__(self, finca=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.finca = finca
        for field in self.fields:
            self.fields[field].required = True

    def save(self, commit=True):
        potrero = super().save(commit=False)
        if self.finca:
            potrero.idfinca = self.finca
        if commit:
            potrero.save()
        return potrero

# Formulario para editar potrero desde la página de finca
class PotreroEditForm(forms.ModelForm):
    class Meta:
        model = Potrero
        fields = ['idfinca', 'nombre', 'area', 'fuenteagua', 'tipopasto']
        widgets = {
            'idfinca': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'area': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'fuenteagua': forms.TextInput(attrs={'class': 'form-control'}),
            'tipopasto': forms.TextInput(attrs={'class': 'form-control'}),
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['idfinca'].queryset = Finca.objects.all().order_by('nombre')

# Formulario para crear potrero desde la página de finca
class PotreroCreateForm(forms.ModelForm):   
    class Meta:
        model = Potrero
        fields = ['idfinca', 'nombre', 'area', 'fuenteagua', 'tipopasto']
        widgets = {
            'idfinca': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'area': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'fuenteagua': forms.TextInput(attrs={'class': 'form-control'}),
            'tipopasto': forms.TextInput(attrs={'class': 'form-control'}),
        }
    def __init__(self, finca=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.finca = finca
        for field in self.fields:
            self.fields[field].required = True

    def save(self, commit=True):
        potrero = super().save(commit=False)
        if self.finca:
            potrero.finca = self.finca
        if commit:
            potrero.save()
        return potrero
    
