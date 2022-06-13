# Integrador22 | Sistema Alumnos
Sistema De Alumnos realizado en Inter-cátedra | Programación y Base de Datos

### Entorno Virtual

Para todos tener las mismas herramientas y framework de django utilizaremos un entorno virtual que cada uno deberá crear. Esto debido a que cada uno de los integrantes del grupo tiene una ruta de instalación de Python distinta.

Pasos a seguir con respecto al *Entorno Virtual* y *REQUERIMENTS.TXT*
* 1) Instalar virtualenv y crear un entorno virtual.
  -  `pip install virtualenv`.
  -  `py -m venv venv`.
* 2) Installar requeriments.txt. 
  -  `pip install -r requirements.txt`.
* 3) Si se installan nuevas herramientas o se actualiza una biblioteca o framework recordar crear un nuevo requeriments.txt.
  -  `pip freeze > requirements.txt.`.

### Django

* Vamos a trabajar con UNA sola APP por API, es decir, la API con la cual trabajes solo va tener UNA APP y todos sus templates,static y urls estarán dentro.
* La carpeta del proyecto principal llamada “SistemaAlumnos” SOLO utilizaremos el archivo “urls.py”.
* El archivo “settings.py” del proyecto (“SistemaAlumnos”) SOLO se modificará las INSTALLED_APPS para agregar la APP.
* UTILIZAREMOS LA NOMENCLATURA camelCase o CamelCase.
Es una práctica de escritura que consiste en la unión de dos o más palabras sin espacios entre ellas, pero las diferencian una letra mayúscula inicial a partir de la segunda palabra, por ejemplo: miNombreEs.

#### Pasos
1) Crearemos la APP y RECORDAR estar en la ruta del proyecto donde se encuentra "manage.py" Documents\GitHub\Integrador22\SistemaAlumnos>
 Ejecutar -> `py manage.py startapp nameApi`.
2) Crear dentro de la APP el archivo "urls.py".

```
from django.urls import path
from nameModule import views

'''
En "urlpatterns" deberas cargar las urls de tu APP.

Ejemplo: path('ejemplo/',views.ejemploview,name="ejemplo")

'''

urlpatterns = [
    path('',views.home,name="Home"),
]

# Esta es la estructura que debe tener el archivo "urls.py" dentro de tu APP.
```

3) Crear en la raiz de la APP la carpeta "templates" y dentro de ella la carpeta con el nombre de la API "nameModule".
```
- templates
  - nameModule
     home.html
             
# La carpeta templates deberia de quedar asi y dentro de nameModule deberá estar todos tus archivos HTML.
# En caso de querer hacer un HTML padre deberás llamar a este de la siguiente manera {% extends 'nameModule/padre.html' %}
```

4) Crear en la raiz de la APP la carpeta llamada "static" y dentro de ella la carpeta con el nombre de la API "nameApi" dentro de la carpeta "nameApi" crear las carpetas "css","js","img".
```
- static
  - nameModule
    - css
       styles.css
    - js
       javaScript.js
    - img
       imagen.png
       
# La carpeta static deberia de quedar asi y dentro de nameModule deberá estar todos tus archivos estaticos en sus 
respectivas carpetas.
# En caso de querer llamar a uno de estos archivos dentro de tu HTML deberás cargar los archivos estaticos primero,
esto al principio antes de la estructura HTML de la siguiente manera {% load static %} 
luego para llamar al archivo deberas de utilizar la siguiente etiqueta DJANGO {% staic 'nameModule/css/ejemplo.css' %} 
esto te devolverá la ruta de tu archivo para que puedas utilizarlo.
```

5) Crear las views 
```
def home(request):
    return render(request,'nameModule/home.html')
```

7. CARGAR LA APP EN "settings.py" DEL PROYECTO PRINCIPAL "SistemaAlumnos".
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nameModule',
]
```

8) EJECUTAR SERVIDOR Y TESTEAR

* Testear la API:
   -> `py manage.py runserver`
   Si la API funciona perfectamente realizar el push, si no, resolver los problemas y luego pushear.
* Realizar el push.
   Primero nos fijaremos si estamos en la ruta de nuestro repositorio en nuestro terminal "Documents\GitHub\Integrador22\" recordar no estar dentro de "SistemaAlumnos". Luego de verificarlo realizaremos los siguientes comandos en el terminal.
```
git status -s 
git add .
git commit -m 'PrimerCommit'
git push origin main
```
