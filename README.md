# SuperTODO 📝

Una aplicación de gestión de tareas sencilla y funcional construida con **Django 6.0**. Este proyecto permite realizar todas las operaciones CRUD (Crear, Leer, Actualizar y Borrar) sobre una lista de tareas personales.

## 🚀 Características

- **Gestión completa de tareas**: Añade, edita, visualiza y elimina tareas.
- **Estado dinámico**: Marca tareas como completadas o pendientes con un solo clic.
- **Formularios robustos**: Uso de `Django ModelForms` para validación y seguridad.
- **Interfaz amigable**: Estilizado con Bootstrap, incluyendo tooltips informativos al pasar el ratón sobre los iconos.
- **URLs amigables**: Uso de `slugs` para la vista de detalle de las tareas.

## 🛠️ Tecnologías utilizadas

- **Backend**: Python 3.13 / Django 6.0.3
- **Frontend**: HTML5, CSS3 (Bootstrap), Emojis como iconos.
- **Base de Datos**: SQLite (por defecto en desarrollo).
- **Control de Versiones**: Git & GitHub.
- **Licencia**: GNU GPL v3.0.

## 📦 Instalación y Configuración

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/FranJGodoy/super-todo.git](https://github.com/FranJGodoy/super-todo.git)
   cd super-todo
2. Crear y activar el entorno virtual:
       Bash
       python -m venv .venv
       source .venv/bin/activate  # En Linux/Mac
3. Instalar dependencias:
       Bash
       pip install django
4. Ejecutar migraciones:
       Bash
       python manage.py migrate
5. Iniciar el servidor:
       Bash
       python manage.py runserver
       Visita http://127.0.0.1:8000/tasks/ en tu navegador.    
📂 Estructura del Proyecto
    • tasks/models.py: Definición del modelo Task (Nombre, Descripción, Slug, Completada).
    • tasks/forms.py: Configuración del ModelForm con widgets de Bootstrap.
    • tasks/views.py: Lógica de negocio (list, detail, create, edit, delete, toggle).
    • tasks/templates/tasks/: Plantillas HTML para la interfaz de usuario.

Creado por FranJGodoy - 2026
