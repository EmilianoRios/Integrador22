from django.shortcuts import render
from BBDD.models import *

# Create your views here.

def materiasAlumnosAulas(request):
    materias = Materia.objects.all() 
    return render(request,'alumnosModulo/materiasHorariosAulas.html', {'materias':materias})

def situacionAcademica(request):
    notas = Nota.objects.all()
    return render(request,'alumnosModulo/situacionAcademica.html', {'notas':notas})