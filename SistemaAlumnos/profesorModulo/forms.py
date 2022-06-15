from django import forms
from django.forms.formsets import formset_factory
from BBDD.models import Nota, Materia
from django.forms import widgets


class NotaForm(forms.ModelForm):
    valorNotaTP1 = forms.IntegerField(label="", widget=forms.Textarea(attrs={'rows':2, 'placeholder':'TP1'}), required=True)
    valorNotaTP2 = forms.IntegerField(label="", widget=forms.Textarea(attrs={'rows':2, 'placeholder':'TP2'}), required=True)
    valorNotaTP3 = forms.IntegerField(label="", widget=forms.Textarea(attrs={'rows':2, 'placeholder':'Parcial'}), required=True)
    valorNotaTP4 = forms.IntegerField(label="", widget=forms.Textarea(attrs={'rows':2, 'placeholder':'Integrador'}), required=True)
    valorNotaFinal = forms.IntegerField(label="", widget=forms.Textarea(attrs={'rows':2, 'placeholder':'Nota final'}), required=True)



    class Meta:
        model = Nota 
        fields = ['valorNotaTP1','valorNotaTP2','valorNotaTP3', 'valorNotaTP4', 'valorNotaFinal', 'materia', 'usuario']