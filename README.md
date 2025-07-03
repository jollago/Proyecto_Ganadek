# Software de Gestión Ganadera con Django y Tailwind CSS

Este proyecto es una aplicación web en desarrollo orientada a la gestión ganadera, construida con Django para el backend y Tailwind CSS junto a FontAwesome para el frontend. Actualmente incluye autenticación de usuarios y gestión de tareas, pero su objetivo principal es convertirse en una solución integral para la administración de fincas ganaderas, permitiendo el registro, control y análisis de información relacionada con el ganado y las actividades productivas.

## Características principales
- Software de gestión ganadera (en desarrollo)
- Backend en Django
- Autenticación de usuarios (registro, inicio de sesión)
- Gestión de tareas
- Frontend moderno con Tailwind CSS
- Iconos con FontAwesome

## Estructura del proyecto
- `Project/`: Configuración principal de Django
- `tasks/`: Aplicación Django para gestión de tareas
- `static/`: Archivos estáticos (CSS, imágenes, iconos)
- `frontend/`: Configuración de Tailwind CSS y dependencias frontend
- `templates/`: Plantillas HTML
- `db.sqlite3`: Base de datos SQLite por defecto

## Instalación
1. Clona el repositorio y entra en la carpeta del proyecto.
2. Instala las dependencias de Python:
   ```bash
   pip install -r requirements.txt
   ```
3. Instala las dependencias de frontend (requiere Node.js y npm):
   ```bash
   cd frontend
   npm install
   cd ..
   ```
4. Aplica las migraciones de la base de datos:
   ```bash
   python manage.py migrate
   ```
5. Ejecuta el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

## Uso
- Regístrate o inicia sesión para gestionar tus tareas

## Personalización
- Modifica los estilos en `frontend/input.css` y ejecuta Tailwind para compilar los cambios.
- Las plantillas HTML están en `tasks/templates/`

## Licencia
Este proyecto es solo para fines educativos y de desarrollo.
