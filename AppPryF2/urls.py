from django.urls import path
from AppPryF2.views import CategoriaListView, UsuarioListView, EntradaListView, EntradaCreateView, CategoriaCreateView, UsuarioCreateView
from AppPryF2.views import saludo, cate, inicio, entrada, categoria, usuario, entradaF, sobreMi, categoriaF, usuarioF, usu, buscarCategoria, buscarC, buscarEntrada 
from AppPryF2.views import editarCategoria, buscarUsuario, buscarE, buscarU, borrarEntrada, borrarUsuario, borrarCategoria, editarEntrada, editarUsuario
from AppPryF2.views import EntradaDetailView, EntradaUpdateView, EntradaDeleteView, CategoriaDetailView, CategoriaDeleteView, CategoriaUpdateView
from AppPryF2.views import UsuarioDeleteView, UsuarioDetailView, UsuarioUpdateView, agregarAvatar, enviarAvatar
from PryF2.views import editarPerfil

urlpatterns = [
    path('saludo', saludo),
    path('nuevaCate', cate),
    path('', inicio, name='inicio'),
    path('editarPerfil', editarPerfil, name='editarPerfil'),
    path('agregarAvatar', agregarAvatar, name='agregarAvatar'),
    path('enviarAvatar', enviarAvatar, name='enviarAvatar'),

    # path('entrada', entrada, name='entrada'),
    path('entrada', EntradaListView.as_view(), name='entrada'),
    # path('entradaF', entradaF),
    path('entradaNueva', EntradaCreateView.as_view(), name='entradaNueva'),
    path('verEntrada/<pk>', EntradaDetailView.as_view(), name='verEntrada'),
    path('updateEntrada/<pk>', EntradaUpdateView.as_view(), name='updateEntrada'),
    path('deleteEntrada/<pk>', EntradaDeleteView.as_view(), name='deleteEntrada'),

    # path('categoria', categoria, name='categoria'),
    path('categoria', CategoriaListView.as_view(), name='categoria'),
    path('categoriaNueva', CategoriaCreateView.as_view(), name='categoriaNueva'),
    path('verCategoria/<pk>', CategoriaDetailView.as_view(), name='verCategoria'),
    path('updateCategoria/<pk>', CategoriaUpdateView.as_view(), name='updateCategoria'),
    path('deleteCategoria/<pk>', CategoriaDeleteView.as_view(), name='deleteCategoria'),
    path('categoriaF', categoriaF, name= 'categoriaF'),
    
    # path('usuario', usuario, name='usuario'),
    path('usuario', UsuarioListView.as_view(), name='usuario'),
    path('usuarioNuevo', UsuarioCreateView.as_view(), name='usuarioNuevo'),
    path('verUsuario/<pk>', UsuarioDetailView.as_view(), name='verUsuario'),
    path('updateUsuario/<pk>', UsuarioUpdateView.as_view(), name='updateUsuario'),
    path('deleteUsuario/<pk>', UsuarioDeleteView.as_view(), name='deleteUsuario'),
    # path('usuarioF', usuarioF),
    # path('usu', usu),
    
    path('sobreMi', sobreMi, name='sobreMi'),
    path('buscarCat', buscarCategoria),
    path('buscarC', buscarC),
    path('buscarUsu', buscarUsuario),
    path('buscarU', buscarU),
    path('buscarEnt', buscarEntrada),
    path('buscarE', buscarE),
    # path('entradaBorrar/<id_entrada>', borrarEntrada, name='borrarEntrada'),
    # path('entradaEditar/<id_entrada>', editarEntrada, name='editarEntrada'),
    # path('usuarioBorrar/<id_usuario>', borrarUsuario, name='borrarUsuario'),
    # path('usuarioEditar/<id_usuario>', editarUsuario, name='editarUsuario'),
    # path('categoriaBorrar/<id_categoria>', borrarCategoria, name='borrarCategoria'),
    # path('categoriaEditar/<id_categoria>', editarCategoria, name='editarCategoria'),
]
