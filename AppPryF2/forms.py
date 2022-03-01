from django import forms
from django.forms import EmailField, CharField, ImageField, PasswordInput, Form

class entradaForm(forms.Form):
    titulo=forms.CharField(max_length=40)
    entrada=forms.CharField()
    nom_usuario=forms.CharField(max_length=50) #Autor del post
    # publicar=forms.BooleanField()
    # fecha_publicacion=forms.DateTimeField()
    # fecha_creacion=forms.DateTimeField()

class categoriaForm(forms.Form):
    nombre_cat=forms.CharField(max_length=40)
    # fecha_creacion=forms.DateTimeField()

class usuarioForm(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    mail=forms.EmailField()
    nom_usuario=forms.CharField(max_length=50)
    clave=forms.CharField(max_length=50)
    # fecha_alta=forms.DateTimeField()

class AvatarFormulario(Form):
    image = ImageField(required=True)
    