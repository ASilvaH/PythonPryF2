from tkinter.tix import Form
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.forms import EmailField, CharField, ImageField, PasswordInput, Form
from django import forms

class UserRegistrationForm(UserCreationForm):
    email = EmailField()
    password1 = CharField(label='Contraseña', widget=PasswordInput)
    password2 = CharField(label='Repetir Contraseña', widget=PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: '' for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label='Modificar email')
    password1 = forms.CharField(label='Contraseña', widget=PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=PasswordInput)
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = {k: '' for k in fields}