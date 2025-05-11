from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class Sign_up(UserCreationForm):
    email = forms.EmailField(required=True, label='Correo Institucional')
    telefono = forms.CharField(max_length=15, required=True, label='Teléfono')
    rol = forms.ChoiceField(choices=[('ESTUDIANTE', 'Estudiante'), ('DOCENTE', 'Docente')], label='Rol')

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'telefono', 'password1', 'password2', 'rol']

class LoginForm(forms.Form):
    username=forms.CharField(max_length=150,label='nombre de usuario',widget=forms.TextInput(attrs={'placeholder':'nombre de usuaario'}))
    password=forms.fields.CharField(max_length=150,label='contaseña',widget=forms.PasswordInput(attrs={'placeholder':'contraseña'}))
