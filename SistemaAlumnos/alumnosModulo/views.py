from django.shortcuts import render

# Create your views here.

def materiasAlumnosAulas(request):
    return render(request,'alumnosModulo/materiasHorariosAulas.html')

def situacionAcademica(request):
    return render(request,'alumnosModulo/situacionAcademica.html')