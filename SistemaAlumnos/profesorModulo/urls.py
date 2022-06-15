from django.urls import path
from profesorModulo import views

'''
En "urlpatterns" deberas cargar las urls de tu APP.

Ejemplo: path('ejemplo/',views.ejemploview,name="ejemplo")

'''

urlpatterns = [
    path('materiasprofesor/',views.materiasProfesor,name="materias_profesor"),
    path('notasprofesor/<id>',views.notasProfesor,name="notas_profesor"),
    path('eliminar_nota/<id>', views.eliminar_notas, name='eliminar_nota'),
    path('agregar_nota',views.agregar_notas, name="agregar_nota"),
    path('editar_nota/<id>/', views.editar_nota, name ='editar_nota'),
]