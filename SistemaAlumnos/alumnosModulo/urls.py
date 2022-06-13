from django.urls import path
from alumnosModulo import views

'''
En "urlpatterns" deberas cargar las urls de tu APP.

Ejemplo: path('ejemplo/',views.ejemploview,name="ejemplo")

'''

urlpatterns = [
    # path('',views.Inicio,name="InicioAlumno"),
    path('situacionAcademica/',views.situacionAcademica,name="SituacionAcademica"),
    path('materias/',views.materiasAlumnosAulas,name="Materias"),
]