from django.db import models
from django.db.models import Model, ImageField, ForeignKey, CASCADE
from django.db.models.fields import BooleanField, CharField, EmailField, IntegerField, DateField, TextField, DateTimeField
from django.contrib.auth.models import User 

class Categoria(Model):
    nombre_cat=CharField(max_length=40)
    fecha_creacion=DateTimeField()

    def __str__(self):
        return f'{self.nombre_cat} {self.fecha_creacion}'


class Entrada(Model):
    titulo=CharField(max_length=40)
    entrada=TextField()
    fecha_creacion=DateTimeField()
    nom_usuario=CharField(max_length=50) #Autor del post
    publicar=BooleanField()
    fecha_publicacion=DateTimeField()
    
    def __str__(self):
        return f'{self.titulo} {self.entrada} {self.fecha_creacion} {self.nom_usuario} {self.publicar} {self.fecha_publicacion}'


class Usuario(Model):
    nombre=CharField(max_length=40)
    apellido=CharField(max_length=40)
    mail=EmailField()
    nom_usuario=CharField(max_length=50)
    clave=CharField(max_length=50)
    fecha_alta=DateTimeField()

    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.mail} {self.nom_usuario} {self.clave} {self.fecha_alta}'


# class Imagenes(Model):
#     nombre_imagen=ImageField(upload_to='imagenes', null=True, blank= True)
#     fecha_upload=DateTimeField()
#     nom_usuario=CharField(max_length=50)
#     titulo=CharField(max_length=40)

#     def __str__(self):
#         return f'{self.nombre_imagen} {self.fecha_upload} {self.nom_usuario} {self.titulo}'

class Avatar(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    imagen = ImageField(upload_to='avatares', null=True, blank = True)
    