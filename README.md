# Sistema de Gestión Universitaria

## Descripción

Sistema de Gestión Universitaria es una aplicación web diseñada para facilitar la gestión de inscripciones en carreras universitarias. Permite a los estudiantes inscribirse en diferentes carreras y gestionar su información académica.

## Características

- **Inscripción en Carreras**: Permite a los estudiantes inscribirse en las carreras disponibles.
- **Gestión de Carreras**: Los administradores pueden agregar, modificar o eliminar carreras.
- **Visualización de Información**: Los estudiantes y administradores pueden ver información relevante sobre las carreras y su inscripción.
- **Interfaz de Usuario Amigable**: Diseñado con una interfaz fácil de usar y responsiva.

## Tecnologías

- **Django**: Framework web en Python.
- **Bootstrap**: Framework CSS para diseño responsivo.
- **SQLite**: Base de datos para almacenamiento (puedes cambiarlo a otro sistema de base de datos si es necesario).

## Instalación

1. **Clonar el repositorio**:
    ```bash
    git clone https://github.com/Romherre/Sistema-de-Gesti-n-Universitaria.git
    ```
2. **Instalar dependencias**:
    Asegúrate de tener [Python](https://www.python.org/downloads/) y [pip](https://pip.pypa.io/en/stable/) instalados. Luego, instala las dependencias del proyecto:
    ```bash
    pip install -r requirements.txt
    ```
3. **Configurar la base de datos**:
    Ejecuta las migraciones para configurar la base de datos:
    ```bash
    python manage.py migrate
    ```
4. **Iniciar el servidor**:
    Ejecuta el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```
    Abre tu navegador y accede a `http://127.0.0.1:8000` para ver la aplicación en acción.

## Uso

- **Página de Inicio**: Accede a la página de inicio para ver la información general.
- **Inscripción**: Navega a la sección de inscripción para inscribirte en una carrera.
- **Administración**: Accede a la sección de administración para gestionar carreras y datos de estudiantes.

.

## Contacto

Si tienes alguna pregunta o sugerencia, no dudes en contactar a:
- **Nombre**: Romina Herrera
- **Correo Electrónico**: romina-herrera@hotmail.com
-  **Linkedin**:https://www.linkedin.com/in/romina-herreramicv/

AVISO Proyecto en poceso se agregaran estilos y login en el futuro
