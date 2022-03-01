from django.shortcuts import render
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from AppPryF2.models import Categoria, Entrada, Usuario, Avatar, User
from datetime import datetime
from AppPryF2.forms import entradaForm, categoriaForm, usuarioForm, AvatarFormulario
from django.core.cache import cache
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class AvatarView():
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['avatar_url'] = Avatar.objects.filter(user=self.request.user).last().imagen.url
        return contexto

def enviarAvatar(request, url=''):
    if request.user.is_anonymous == False:
        avatares = Avatar.objects.filter(user=request.user)
        if avatares:
            avatar_url = avatares.last().imagen.url
        else:
            avatar_url = ''
    return (avatar_url)

def saludo(request):
    return HttpResponse('Hola :(')

def cate(self):
    cate = Categoria(nombre_cat='Animales', fecha_creacion=datetime.now())
    cate.save()
    doc = f"Curso nuevo: {cate.nombre_cat} y Fecha de creación: {cate.fecha_creacion}"
    return HttpResponse(doc)

def usu(self):
    usu = Usuario(nombre='Ariana', apellido='Fernandez', nom_usuario='arif', mail='ari@a.cl', clave='a12', fecha_alta=datetime.now())
    usu.save()
    doc = f"Usuario nuevo: {usu.nombre} {usu.apellido}. Mail: {usu.mail} y Fecha de creación: {usu.fecha_alta}"
    return HttpResponse(doc)

def inicio(request):

    if request.user.is_anonymous == False:
        avatares = Avatar.objects.filter(user=request.user)
        if avatares:
            avatar_url = avatares.last().imagen.url
        else:
            avatar_url = ''
        return render(request, 'inicio.html', {'avatar_url':avatar_url})
    else:
        return render(request, 'inicio.html', {'avatar_url':''})    

def categoria(request):
    return render(request, 'categoria.html', {'categorias': Categoria.objects.all()})

def usuario(request):
    return render(request, 'usuario.html', {'usuarios': Usuario.objects.all()})

def entrada(request):
    return render(request, 'entrada.html', {'entradas': Entrada.objects.all()})

def buscarCategoria(request):
        avatar_url = enviarAvatar(request, 'buscarCat.html')
        return render(request, 'buscarCat.html', {'avatar_url':avatar_url})

def buscarC(request):    
    if request.GET['nombre_cat']:
        cat = request.GET['nombre_cat']
        categ = Categoria.objects.filter(nombre_cat__icontains=cat)
        avatar_url = enviarAvatar(request, 'buscarC.html')
        return render(request, 'buscarC.html', {'categorias':categ}, {'avatar_url':avatar_url})

def buscarUsuario(request):
        avatar_url = enviarAvatar(request, 'buscarUsu.html')
        return render(request, 'buscarUsu.html', {'avatar_url':avatar_url})

def buscarU(request):    
    if request.GET['nom_usuario']:
        usu = request.GET['nom_usuario']
        usuar = Usuario.objects.filter(nom_usuario__icontains=usu)
        return render(request, 'buscarU.html', {'usuarios':usuar})

def buscarEntrada(request):
        avatar_url = enviarAvatar(request, 'buscarUsu.html')
        return render(request, 'buscarEnt.html', {'avatar_url':avatar_url})

def buscarE(request):    
    if request.GET['titulo']:
        titu = request.GET['titulo']
        entra = Entrada.objects.filter(titulo__icontains=titu)
        return render(request, 'buscarE.html', {'entradas':entra})

@login_required
def sobreMi(request):
    avatar_url = enviarAvatar(request, 'sobreMi.html')
    return render(request, 'sobreMi.html', {'avatar_url':avatar_url})

def entradaF(request):
    if request.method == 'POST':
        miForm = entradaForm(request.POST)

        if miForm.is_valid():
                infor = miForm.cleaned_data
                entrada = Entrada(titulo =infor['titulo'], entrada =infor['entrada'], nom_usuario =infor['nom_usuario'], publicar = True, 
                fecha_creacion = datetime.now(), fecha_publicacion = datetime.now())
                entrada.save()
                cache.clear()
                return redirect(entrada)
    else:
        miForm = entradaForm()
    return render(request, 'entradaForm.html', {'miForm':miForm})

def categoriaF(request):
    if request.method == 'POST':
        miFormu = categoriaForm(request.POST)

        if miFormu.is_valid():
                infor = miFormu.cleaned_data
                categoria = Categoria(nombre_cat =infor['nombre_cat'], fecha_creacion = datetime.now())
                categoria.save()
                return redirect(categoria)

    else:
        miFormu = categoriaForm()
    return render(request, 'categoriaForm.html', {'miFormu':miFormu})    

def usuarioF(request):
    if request.method == 'POST':
        formUsu = usuarioForm(request.POST)

        if formUsu.is_valid():
                informacion = formUsu.cleaned_data
                usuario1 = Usuario(nombre =informacion['nombre'], apellido =informacion['apellido'], nom_usuario =informacion['nom_usuario'], mail =informacion['mail'], fecha_alta = datetime.now())
                usuario1.save()
                return redirect(usuario)
    else:
        formUsu = usuarioForm()
    return render(request, 'usuarioForm.html', {'formUsu':formUsu})

@login_required
def borrarEntrada(request, id_entrada):
    entBorrar = Entrada.objects.get(id=id_entrada)
    entBorrar.delete()
    return redirect(entrada)

@login_required
def borrarUsuario(request, id_usuario):
    usuBorrar = Usuario.objects.get(id=id_usuario)
    usuBorrar.delete()
    return redirect(usuario)

@login_required
def borrarCategoria(request, id_categoria):
    catBorrar = Categoria.objects.get(id=id_categoria)
    catBorrar.delete()
    return redirect(categoria)

@login_required
def editarEntrada(request, id_entrada):

    ent = Entrada.objects.get(id=id_entrada)

    if request.method == 'POST':
        miForm = entradaForm(request.POST)

        if miForm.is_valid():
                infor = miForm.cleaned_data
                ent.titulo =infor['titulo'] 
                ent.entrada =infor['entrada']
                ent.nom_usuario =infor['nom_usuario']
                ent.publicar = True
                ent.fecha_publicacion = datetime.now()
                ent.save()
                return redirect(entrada)

    else:
        miForm = entradaForm(model_to_dict(ent))
        
    return render(request, 'entradaForm.html', {'miForm':miForm})

@login_required
def editarUsuario(request, id_usuario):

    usu = Usuario.objects.get(id=id_usuario)

    if request.method == 'POST':
        formUsu = usuarioForm(request.POST)

        if formUsu.is_valid():
                informacion = formUsu.cleaned_data
                usu.nombre =informacion['nombre'] 
                usu.apellido =informacion['apellido']
                usu.nom_usuario =informacion['nom_usuario']
                usu.mail =informacion['mail']
                usu.clave =informacion['clave']
                usu.save()
                return redirect(usuario)

    else:
        formUsu = usuarioForm(model_to_dict(usu))

    return render(request, 'usuarioForm.html', {'formUsu':formUsu}) 

@login_required
def editarCategoria(request, id_categoria):

    cate = Categoria.objects.get(id=id_categoria)

    if request.method == 'POST':
        miFormu = categoriaForm(request.POST)

        if miFormu.is_valid():
                infor = miFormu.cleaned_data
                cate.nombre_cat = infor['nombre_cat']
                cate.fecha_creacion = datetime.now()
                cate.save()
                return redirect(categoria)

    else:
        miFormu = categoriaForm(model_to_dict(cate))
    
    return render(request, 'categoriaForm.html', {'miFormu':miFormu})    

class CategoriaListView (LoginRequiredMixin, AvatarView, ListView):
    model = Categoria
    template_name = 'categoria.html'

class EntradaListView (LoginRequiredMixin, AvatarView, ListView):
    model = Entrada        
    template_name = 'entrada.html'

class UsuarioListView (LoginRequiredMixin, AvatarView, ListView):
    model = Usuario
    template_name = 'usuario.html'

class EntradaDetailView (LoginRequiredMixin, AvatarView, DetailView):
    model = Entrada
    template_name = 'verEntrada.html'
    context_object_name = 'entrada'

class EntradaCreateView(LoginRequiredMixin, AvatarView, CreateView): 
    model = Entrada
    success_url = reverse_lazy('entrada')
    fields = ['titulo', 'entrada', 'nom_usuario', 'fecha_creacion', 'publicar', 'fecha_publicacion']
    template_name = 'crearEntrada.html'

class EntradaUpdateView(LoginRequiredMixin, AvatarView, UpdateView): 
    model = Entrada
    success_url = reverse_lazy('entrada')
    fields = ['titulo', 'entrada', 'nom_usuario', 'fecha_creacion', 'publicar', 'fecha_publicacion']
    template_name = 'crearEntrada.html'

class EntradaDeleteView(LoginRequiredMixin, AvatarView, DeleteView):
    model = Entrada
    success_url = reverse_lazy('entrada')
    template_name = 'borrarEntrada.html'
    # template_name toma por defecto '/profesor_confirm_delete.html'

class CategoriaCreateView(LoginRequiredMixin, AvatarView, CreateView): 
    model = Categoria
    success_url = reverse_lazy('categoria')
    fields = ['nombre_cat', 'fecha_creacion']
    template_name = 'crearCategoria.html'

class CategoriaDetailView (LoginRequiredMixin, AvatarView, DetailView):
    model = Categoria
    template_name = 'verCategoria.html'
    context_object_name = 'categoria'

class CategoriaUpdateView(LoginRequiredMixin, AvatarView, UpdateView): 
    model = Categoria
    success_url = reverse_lazy('categoria')
    fields = ['nombre_cat', 'fecha_creacion']
    template_name = 'crearCategoria.html'

class CategoriaDeleteView(LoginRequiredMixin, AvatarView, DeleteView):
    model = Categoria
    success_url = reverse_lazy('categoria')
    template_name = 'borrarCategoria.html'
    # template_name toma por defecto '/profesor_confirm_delete.html'

class UsuarioCreateView(LoginRequiredMixin, AvatarView, CreateView): 
    model = Usuario
    success_url = reverse_lazy('usuario')
    fields = ['nombre', 'apellido', 'nom_usuario', 'mail', 'clave', 'fecha_alta']
    template_name = 'crearUsuario.html'    

class UsuarioDetailView (LoginRequiredMixin, AvatarView, DetailView):
    model = Usuario
    template_name = 'verUsuario.html'
    context_object_name = 'usuario'

class UsuarioUpdateView(LoginRequiredMixin, AvatarView, UpdateView): 
    model = Usuario
    success_url = reverse_lazy('usuario')
    fields = ['nombre', 'apellido', 'nom_usuario', 'mail', 'clave', 'fecha_alta']
    template_name = 'crearUsuario.html'

class UsuarioDeleteView(LoginRequiredMixin, AvatarView, DeleteView):
    model = Usuario
    success_url = reverse_lazy('usuario')
    template_name = 'borrarUsuario.html'
    # template_name toma por defecto '/profesor_confirm_delete.html'

@login_required
def agregarAvatar(request):

    if request.method == 'POST':
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            avatar = Avatar(user = request.user, imagen = form.cleaned_data['image'])
            avatar.save()

            return redirect(inicio)
    else:
        form=AvatarFormulario()

    return render(request, 'agregarAvatar.html', {'form':form})            

