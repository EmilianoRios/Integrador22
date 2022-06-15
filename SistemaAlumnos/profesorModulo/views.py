from django.shortcuts import get_object_or_404, render, redirect
from BBDD.models import *
from .forms import NotaForm

def materiasProfesor(request):
    materias = Materia.objects.all()
    notas = Nota.objects.all()
    context = {'materias':materias,'notas':notas }
    return render(request, 'profesorModulo/materias.html', context)

def notasProfesor(request,id):
    filtroNota =  Nota.objects.filter(materia=id)
    context = {'notas':filtroNota}
    return render(request,'profesorModulo/notas.html',context)

def eliminar_notas(request,id):
    notas = get_object_or_404(Nota,id=id)
    notas.delete()
    return redirect('/materiasprofesor')

def agregar_notas(request):
    if request.method == "POST":
        form = NotaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/materiasprofesor')
    else:
        form = NotaForm()
    return render(request, 'profesorModulo/agregar_nota.html', {'form': form})

def editar_nota(request,id):
    nota = get_object_or_404(Nota,id=id)
    
    contexto = {
        'form':NotaForm(instance=nota)
    }
    
    if request.method=='POST':
        formulario = NotaForm(data=request.POST, instance=nota)
        if formulario.is_valid():
            formulario.save()
            return redirect('/notasprofesor')
        contexto['form'] = formulario

    return render(request,'profesorModulo/editar_nota.html', contexto)


