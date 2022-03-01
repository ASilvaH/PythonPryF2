from django.contrib import admin

from AppPryF2.models import Categoria, Usuario, Entrada, Avatar

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Entrada)
admin.site.register(Usuario)
admin.site.register(Avatar)