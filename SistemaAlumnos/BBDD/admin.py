from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()


admin.site.register(Usuario)
admin.site.register(Pais)
admin.site.register(Provincia)
admin.site.register(Localidad)
admin.site.register(Domicilio)
admin.site.register(Contacto)
admin.site.register(Universidad)
admin.site.register(Sede)
admin.site.register(Ubicacion)
admin.site.register(Facultad)
admin.site.register(Carrera)
admin.site.register(Materia)
admin.site.register(Nota)



