from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms import widgets

User = get_user_model()

class UserRegisterForm(forms.ModelForm):

    username = forms.CharField(label='Usuario',widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su usuario'}))
    email = forms.EmailField(label='Correo', widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Ingrese su correo'}))
    first_name = forms.CharField(label='first_name', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='last_name', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Ingrese su contraseña'}))
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirme su contraseña'}))

    class Meta:
        model = User
        fields = ['username','email', 'first_name', 'last_name','password', 'password2']
        help_texts = {k:"" for k in fields}
