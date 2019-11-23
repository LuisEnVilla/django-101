# django-101

proyecto de diplomado en Django

## Inital project

´´´text
Build DB container: >docker-compose build db
1. Bring DB container up: >docker-compose up db
    1. Set DB container to run on background:  >docker-compose up -d db
1. Build MIGRATIONS container: >docker-compose build migration
1. Build WEB container: >docker-compose build web
1. Create a Django Project: >docker-compose run web django-admin startproject my_web
1. Setup DB connection on settings.py file
1. Run MIGRATIONS container to create db >docker-compose up migration
1. Run Web container to check if settings and db are working: >docker-compose up web
1. Create a Super User for Admin: >docker-compose run web python my_web/manage.py createsuperuser

**Helpfull Commands**
1. Create migrations for a specific app: >docker-compose run migration python my_web/manage.py makemigrations <APP_NAME>
1. Open Django Shell: >docker-compose run migration python my_web/manage.py shell
´´´

## Run Project

Despues de compilar todo en docker necesitamos

### DB

´´´shell
docker-compose up -d db
´´´

### Server

´´´shell
docker-compose up web
´´´

### Add Model

Migra el modelo a la DB para generar las tablas correspondientes.

´´´shell
docker-compose run migration python my_web/manage.py makemigrations <APP_NAME>
docker-compose run migration python my_web/manage.py migrate
´´´

### Exportar de Docker Template

- Clonar de docker-template/apps/{modelo}
- Agregar en my_web/settings.py 

´´´python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'my_web.personas',
    'my_web.estudios'
    ...
]
´´´

- En consola correr la migración

´´´shell
docker-compose run migration python my_web/manage.py makemigrations <APP_NAME>
docker-compose run migration python my_web/manage.py migrate
´´´