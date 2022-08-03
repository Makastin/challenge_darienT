# Funcionalidades del Backend

## Estructura del Proyecto
Laa idea principal del proyecto es agilizar la problematica planteada a la empresa `Tu Credito`,
la cual mantienen registros multiples de forma manual y no cuentan con la tecnologia para mantener 
de una forma sistematizada, la creacion y seguimiento rapido de la emision de creditos a sus clientes
a traves de bancos que ofrezcan dicho servicio.

La forma en la que estaestructurado el proyecto, permite la rapida emision de creditos a sus clientes
previamente registrados, asignandoles un banco que permita la autorizacion del credito

## Archivos/Estructura de archivos

El proyecto esta estructurado en una diversidad minima de apps que, pemriten ejercer de forma organizada
los requerimientos que se plantean dentro del desarrollo. Estas apps son:

- banks
- clients
- credits
- core

Cada una de las apps, contienen archivos de configuracion que son:

- models.py
- views.py
- forms.py
- urls.py

Los cuales contienen las configuraciones respectivas
Cada una de las apps mencionadas, ejercen un proceso distinto y unico dentro el proyecto, en caso contratio de la
app `core`, la cual mantiene la configracion completa del proyecto y se divide de la siguiente forma:

- wsgi.py
- asgi.py
- settings.py
- urls.py


## Ejecucion y funcionamiento del proyecto

El proyecto esta configurado para funcionar en un contenedor de `docker`

Ejecuta el siguente comandos:

```bash
$ docker-compose up
```

Mediante ese comando se ejecera la instalacion de todas las dependencias necesarias para hacer funcionar el proyecto



## Usuarios, accesos, procesos

El acceso al proyecto, esta planteado solo para acceder para personar que sean adminitradores dentro del mismo, no cuenta
con un modulo desarrollado de manejo de usuarios a clientes. Se utiliza el modelo de usuarios por defecto que implementa Django.

Por defecto al hacer funcionar el proyecto, se crean las siguientes credenciales:

- usuario: admin@localhost.com
- correo: admin@localhost.com
- contraseña: 4321Admin

## Testing

Para el proyecto se utiliza [`pytest`](https://docs.pytest.org/en/latest/) con
 [`pytest-django`](https://pytest-django.readthedocs.io/en/latest/), Python/Django UnitTest esta deshabilitado.


## Manejo de paquetes

Para el proyecto se usa [`Pipenv`](https://docs.pipenv.org/en/latest/).

## Antes de ejercer algun commit

Ejecuta los siguentes comandos:

```bash
$ isort . -m 3 -l 120
$ flake8
```

Checklist:

- [ ] no issues found by `isort` and `flake8`
- [ ] all tests passed


# Models

#### Clients
![Client app](/challenge_django/models_structure/clients.png?raw=true "Client app")

#### Credits
![Credits app](/challenge_django/models_structure/credits.png?raw=true "Credits app")

#### Banks
![Banks app](/challenge_django/models_structure/banks.png?raw=true "Bank app")

#### Project Structure
![Projetc Structure](/challenge_django/models_structure/project.png?raw=true "Project Structure")
