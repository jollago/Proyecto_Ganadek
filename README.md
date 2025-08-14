# 🐄 Software de Gestión Ganadera - Ganadek

Este proyecto es una aplicación web en desarrollo orientada a la gestión ganadera, construida con **Django** para el backend y **Tailwind CSS** junto a **FontAwesome** para el frontend. Actualmente incluye autenticación de usuarios y gestión de tareas, pero su objetivo principal es convertirse en una solución integral para la administración de fincas ganaderas, permitiendo el registro, control y análisis de información relacionada con el ganado y las actividades productivas.

![Estado del Proyecto](https://img.shields.io/badge/Estado-En%20Desarrollo-yellow)
![Django](https://img.shields.io/badge/Django-4.x-green)
![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-3.x-blue)

## 🎯 Estado del Proyecto

### ✅ Funcionalidades Completadas
- **Autenticación de usuarios**: Sistema de login seguro
- **Gestión de fincas**: Registro y administración de fincas
- **Unidades productivas**: Gestión de galpones, jaulas y potreros
- **Módulo de animales**: Registro y control básico de animales
- **Gestión de usuarios**: CRUD completo de usuarios del sistema
- **Gestión de perfil**: Edición de datos personales y cambio de contraseña
- **Dashboard básico**: Interfaz principal con navegación
- **Base de datos**: Configuración con MySQL
- **Frontend moderno**: Diseño responsivo con Tailwind CSS
- **Sistema de iconos**: Integración con FontAwesome

### 🚧 En Proceso de Desarrollo
- **Reportes básicos**: Estadísticas de producción y animales
- **Calendario de actividades**: Programación avanzada de tareas
- **Mejoras en módulo de animales**: Funcionalidades adicionales
- **Control reproductivo**: Seguimiento de apareamientos y partos
- **Historial médico**: Registro de vacunas y tratamientos
- **Inventario de insumos**: Control de alimentos y medicamentos

### 📋 Funcionalidades Planificadas
- **Gestión de empleados**: Control de personal de la finca
- **Análisis de costos**: Control financiero de la operación
- **Alertas automáticas**: Notificaciones de eventos importantes
- **Exportación de datos**: Reportes en PDF y Excel
- **App móvil**: Aplicación para dispositivos móviles

## 🛠️ Tecnologías Utilizadas

### Backend
- **Django 4.x**: Framework web de Python
- **MySQL**: Base de datos relacional
- **Python**: Lenguaje de programación principal

### Frontend
- **Tailwind CSS 3.x**: Framework de CSS utility-first
- **FontAwesome**: Biblioteca de iconos
- **HTML5 & JavaScript**: Tecnologías web estándar

### Herramientas de Desarrollo
- **Node.js & npm**: Para gestión de dependencias frontend
- **Git**: Control de versiones

## 📁 Estructura del Proyecto

```
Proyecto_Ganadek/
├── Project/                # Configuración principal de Django
│   ├── settings.py        # Configuraciones del proyecto
│   ├── urls.py           # URLs principales
│   └── wsgi.py           # Configuración WSGI
├── tasks/                 # Aplicación Django para gestión de tareas
│   ├── models.py         # Modelos de datos
│   ├── views.py          # Vistas y lógica
│   ├── urls.py           # URLs de la aplicación
│   └── templates/        # Plantillas HTML específicas
├── static/               # Archivos estáticos
│   ├── css/             # Estilos compilados
│   ├── images/          # Imágenes del proyecto
│   └── icons/           # Iconos personalizados
├── frontend/             # Configuración frontend
│   ├── input.css        # Estilos base de Tailwind
│   ├── package.json     # Dependencias Node.js
│   └── tailwind.config.js # Configuración de Tailwind
├── templates/            # Plantillas HTML globales
│   ├── base.html        # Plantilla base
│   └── registration/    # Plantillas de autenticación
├── requirements.txt     # Dependencias del Proyecto
└── manage.py           # Script de gestión de Django
```

## ⚙️ Instalación y Configuración

### Prerrequisitos
- Python 3.8 o superior
- Node.js 16 o superior
- MySQL 8.0 o superior
- Git

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/jollago/Proyecto_Ganadek.git
   cd Proyecto_Ganadek
   ```

2. **Crear y activar entorno virtual (recomendado)**
   ```bash
   python -m venv venv
   
   # En Windows
   venv\Scripts\activate
   
   # En macOS/Linux
   source venv/bin/activate
   ```

3. **Instalar dependencias de Python**
   ```bash
   pip install -r requirements.txt
   ```

4. **Instalar dependencias del frontend**
   ```bash
   cd frontend
   npm install
   cd ..
   ```

5. **Configurar la base de datos**
   - Crea una base de datos MySQL llamada `ganadek`
   - Actualiza las credenciales en `Project/settings.py`
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'ganadek',
           'USER': 'tu_usuario',
           'PASSWORD': 'tu_contraseña',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

6. **Aplicar migraciones**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
   
7. **Compilar estilos de Tailwind**
   ```bash
   cd frontend
   npm run build-css
   cd ..
   ```

8. **Ejecutar servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```

La aplicación estará disponible en `http://localhost:8000`

## 🚀 Cómo Usar el Sistema

### 🔐 Acceso al Sistema

**IMPORTANTE**: El registro público está deshabilitado por seguridad. Para acceder al sistema:

1. **Contacta al administrador** para solicitar una cuenta de usuario
2. **Proporciona la siguiente información**:
   - Nombre completo
   - Email de contacto
   - Razón del acceso (nombre de la finca, empresa, etc.)
   - Nivel de acceso requerido

3. **Una vez creada tu cuenta**:
   - Ve a `http://localhost:8000/login`
   - Ingresa con las credenciales proporcionadas
   - Serás redirigido al dashboard principal

### 📊 Dashboard Principal

Una vez autenticado, tendrás acceso a:
- **Resumen general**: Estadísticas básicas del sistema
- **Accesos rápidos**: Enlaces a las funcionalidades principales
- **Navegación principal**: Menú para acceder a todos los módulos

### 🏢 Gestión de Fincas

#### Registrar una Nueva Finca
1. Ve a la sección **"Fincas"** desde el menú principal
2. Haz clic en **"Agregar Nueva Finca"**
3. Completa la información:
   - **Nombre**: Nombre de la finca
   - **Ubicación**: Dirección o coordenadas
   - **Área total**: Extensión en hectáreas
   - **Tipo de producción**: Ganadería, avicultura, etc.
   - **Descripción**: Información adicional
   - **Rellenar datos requeridos**
4. Guarda la finca

#### Gestionar Fincas Existentes
- **Lista de fincas**: Visualiza todas las fincas registradas
- **Ver detalles**: Información completa de cada finca
- **Editar información**: Actualizar datos de la finca
- **Eliminar finca**: Con confirmación de seguridad

### 🏗️ Unidades Productivas

#### Tipos de Unidades Disponibles
- **Potreros**: Para ganado bovino, ovino, etc.
- **Galpones**: Para aves, cerdos, etc.
- **Jaulas**: Para cría intensiva

#### Crear una Unidad Productiva
1. Selecciona la **finca** donde se ubicará
2. Ve a **"Unidades Productivas"** 
3. Haz clic en **"Agregar Nueva Unidad"**
4. Completa los datos:
   - **Nombre/Código**: Identificación única
   - **Tipo**: Potrero, galpón o jaula
   - **Capacidad**: Número máximo de animales
   - **Área**: Dimensiones o metros cuadrados
   - **Estado**: Activa, en mantenimiento, etc.
   - **Rellenar datos requeridos**
5. Asigna la unidad a la finca correspondiente

#### Gestionar Unidades Productivas
- **Visualizar por finca**: Ve todas las unidades de una finca específica
- **Control de ocupación**: Monitora cuántos animales hay por unidad
- **Editar unidades**: Actualiza información y capacidades
- **Cambiar estado**: Marcar como activa, inactiva, en mantenimiento

### 🐄 Gestión de Animales

#### Registrar un Nuevo Animal
1. Ve a la sección **"Animales"**
2. Haz clic en **"Agregar Nuevo Animal"**
3. Completa la información básica:
   - **Identificación**: Número de arete o código único
   - **Especie**: Bovino, ovino, porcino, ave, etc.
   - **Raza**: Especifica la raza del animal
   - **Unidad productiva**: Asigna donde se encuentra
   - - **Rellenar datos requeridos**
4. Información adicional:
   - **Estado**: Activo, vendido, fallecido, etc.
5. Guarda el registro

#### Ver y Gestionar Animales
- **Lista completa**: Todos los animales registrados
- **Ver detalles**: Información completa del animal
- **Editar información**: Actualizar peso, ubicación, estado
- **Mover animal**: Cambiar de unidad productiva
- **Eliminar registro**: Con confirmación

#### Control por Unidad Productiva
- **Ocupación actual**: Cuántos animales hay en cada unidad
- **Capacidad disponible**: Espacio restante
- **Lista por unidad**: Ver todos los animales de una unidad específica

### 👥 Gestión de Usuarios

#### Crear Nuevos Usuarios (Solo Administrador)
1. Ve a **"Gestión de Usuarios"**
2. Haz clic en **"Crear Usuario"**
3. Completa los datos:
   - **Nombre de usuario**: Para el login
   - **Email**: Correo electrónico
   - **Nombre completo**: Nombre real del usuario
   - **Contraseña temporal**: El usuario deberá cambiarla
   - **Nivel de acceso**: Administrador, Usuario estándar, Solo lectura
   - **Fincas asignadas**: A cuáles fincas tiene acceso
4. Envía las credenciales al nuevo usuario

#### Administrar Usuarios Existentes
- **Lista de usuarios**: Todos los usuarios del sistema
- **Ver perfiles**: Información completa de cada usuario
- **Editar permisos**: Cambiar nivel de acceso o fincas asignadas
- **Desactivar usuario**: Suspender acceso temporalmente
- **Eliminar usuario**: Borrar cuenta permanentemente
- **Resetear contraseña**: Generar nueva contraseña temporal

### ⚙️ Gestión de Perfil Personal

#### Actualizar Información Personal
1. Haz clic en tu **nombre de usuario** (esquina superior derecha)
2. Selecciona **"Mi Perfil"**
3. Puedes editar:
   - **Nombre completo**
   - **Email de contacto**
   - **Teléfono** (si aplica)
   - **Información adicional**

#### Cambiar Contraseña
1. En tu perfil, ve a **"Cambiar Contraseña"**
2. Ingresa:
   - **Contraseña actual**: Para verificar identidad
   - **Nueva contraseña**: Debe ser segura
   - **Confirmar nueva contraseña**: Para evitar errores
3. Guarda los cambios
4. Serás redirigido al login para iniciar sesión nuevamente


### 🚧 Módulos en Desarrollo

#### Sistema de Reportes (En desarrollo)
- **Estado**: Función en proceso de creación
- **Funcionalidad planeada**:
  - Reportes de animales por finca y unidad productiva
  - Estadísticas de ocupación de unidades
  - Análisis de productividad por tipo de animal
  - Reportes de tareas completadas vs pendientes

#### Mejoras en Módulo de Animales (En proceso)
- **Estado**: Expandiendo funcionalidades existentes
- **Próximas mejoras**:
  - Historial de movimientos entre unidades
  - Registro fotográfico de animales
  - Control de peso histórico
  - Alertas automáticas por sobrepoblación

## 🎨 Personalización del Frontend

### Modificar Estilos
1. **Edita los estilos** en `frontend/input.css`
2. **Compila los cambios**:
   ```bash
   cd frontend
   npm run build-css
   ```
3. **Los estilos compilados** se guardan en `static/css/`

### Configuración de Tailwind
- **Archivo de configuración**: `frontend/tailwind.config.js`
- **Colores personalizados**: Modifica la paleta según tu marca
- **Breakpoints**: Ajusta los puntos de quiebre responsivos

### Plantillas HTML
- **Plantilla base**: `templates/base.html`
- **Plantillas específicas**: `tasks/templates/`
- **Componentes reutilizables**: Crea parciales para elementos comunes

## 👥 Niveles de Usuario

### Administrador
- Acceso completo al sistema
- Gestión de usuarios
- Configuración del sistema
- Acceso a todos los módulos

### Usuario Estándar
- Gestión de tareas propias
- Visualización de reportes básicos
- Acceso limitado según permisos asignados

### Usuario de Solo Lectura
- Visualización de información
- Sin permisos de edición
- Ideal para supervisores o consultores

## 📞 Contacto y Soporte

### Para Solicitar Acceso
- **Desarrollador**: [@jollago](https://github.com/jollago)
- **Email**: Joseluisllanos815@gmail.com
- **Asunto**: "Solicitud de acceso - Ganadek"

### Información a Proporcionar
- Nombre completo
- Organización/Finca
- Email de contacto
- Teléfono (opcional)
- Descripción del uso previsto

## 🐛 Reportar Problemas

Si encuentras errores o tienes sugerencias:
1. Ve a [Issues](https://github.com/jollago/Proyecto_Ganadek/issues)
2. Crea un nuevo issue con:
   - Descripción del problema
   - Pasos para reproducirlo
   - Capturas de pantalla si aplica
   - Información del navegador/sistema

## 🚀 Roadmap de Desarrollo

### Versión 1.0 (Actual)
- [x] Sistema de autenticación
- [x] Gestión de fincas
- [x] Gestión de unidades productivas (potreros, galpones, jaulas)
- [x] Módulo básico de animales
- [x] Gestión completa de usuarios
- [x] Gestión de perfil personal y cambio de contraseña
- [x] Dashboard principal
- [x] Frontend con Tailwind CSS

### Versión 2.0 (Próximos 3-6 meses)
- [ ] Sistema de reportes y estadísticas
- [ ] Mejoras en el módulo de animales
- [ ] Gestión de empleados
- [ ] Control de inventarios básico
- [ ] Mejoras en la interfaz de usuario
- [ ] Sistema de notificaciones

### Versión 3.0 (Futuro)
- [ ] App móvil para Android/iOS
- [ ] API RESTful completa
- [ ] Integración con dispositivos IoT
- [ ] Análisis predictivo con IA
- [ ] Sistema de facturación

## 📄 Licencia

Este proyecto está desarrollado con fines educativos y de aprendizaje. 

**Uso Educativo**: Permitido para estudios y desarrollo personal
**Uso Comercial**: Contactar al desarrollador para licencias comerciales

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Áreas donde puedes ayudar:
- 🐛 Corrección de bugs
- ✨ Nuevas funcionalidades
- 📝 Documentación
- 🎨 Mejoras en el diseño
- 🧪 Pruebas y testing
- $ paypal :llanosgomezjoseluis815qgmail.com
- $ Nequi : 3042224964
- $ Davivienda : 3112160323

### Proceso de Contribución
1. Haz fork del repositorio
2. Crea una rama para tu feature
3. Realiza tus cambios
4. Envía un pull request

---

⭐ **¡Dale una estrella si te parece útil este proyecto!**

**Última actualización**: Agosto 2025
