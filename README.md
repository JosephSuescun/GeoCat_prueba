Comandos relevantes
Instalacion entorno virtual
pip install virtualenv
Creacion entorno virtual 
virtualenv venv
Activación del entorno
virtualenv venv
Instalamos django solo en este proyecto 
pip install django 
Creamos el proyecto 
django-admin startproject NOMBRE_PROYECTO
Crear app
python manage.py startapp
Crear migraciones 
python manage.py makemigrations
Aplicar migraciones
python manage.py migrate
Crear el superuser
python manage.py createsuperuser
Instalar dependencias:

pip install -r requirements.txt
Configuración de la base de datos
Este proyecto utiliza PostgreSQL como base de datos. Asegúrate de tener PostgreSQL instalado y configurado en tu máquina. Luego, configura la base de datos en GeoAdmin/settings.py:

python
Copiar código
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'GeoAdmin',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Archivos importantes
settings.py: Configuración principal del proyecto Django, incluyendo configuración de base de datos, aplicaciones instaladas, middleware, etc.

urls.py: Gestiona las URL del proyecto, incluyendo rutas para las vistas y APIs de las aplicaciones.

admin.py: Configuración de administración de Django para registrar modelos y hacerlos accesibles en el panel de administración.

models.py: Define los modelos de la base de datos utilizando Django ORM. Incluye modelos como Municipality, Entity, Dependency y Producer con relaciones entre ellos.

serializers.py: Define los serializadores para convertir los modelos de Django en JSON y viceversa. Incluye MunicipalitySerializer, EntitySerializer, DependencySerializer y ProducerSerializer.

views.py: Contiene las vistas que manejan las solicitudes HTTP, utilizando Django Rest Framework para implementar operaciones CRUD para cada modelo.

Comandos útiles
Ejecutar migraciones: python manage.py migrate
Crear superusuario: python manage.py createsuperuser
Ejecutar servidor de desarrollo: python manage.py runserver
Ejemplos de uso
API Endpoints
Listar y crear municipios:

bash
Copiar código
GET /municipalities/
POST /municipalities/
Obtener detalles de un municipio por nombre:

bash
Copiar código
GET /municipalities/{nombre}/
Actualizar y borrar un municipio por ID:

bash
Copiar código
PUT /municipalities/update/{id}/
DELETE /municipalities/delete/{id}/
