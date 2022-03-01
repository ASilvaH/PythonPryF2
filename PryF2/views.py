from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from PryF2.forms import UserRegistrationForm, UserEditForm
from django.contrib.auth import login, logout, authenticate
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from AppPryF2.models import Avatar

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuarioLogin = form.cleaned_data.get('username')
            contraLogin = form.cleaned_data.get('password')

            user = authenticate(username = usuarioLogin, password = contraLogin)

            if user is not None:
                login(request, user)
                avatares = Avatar.objects.filter(user=request.user)
                if avatares:
                    avatar_url = avatares.last().imagen.url
                else:
                    avatar_url = ''
            return render(request, 'inicio.html', {'usuarioLogin': f'{usuarioLogin}', 'avatar_url':avatar_url})
        else:
            return render(request, 'login.html', {'form': form, 'mensaje': 'Error: Datos incorrectos'})        

    form = AuthenticationForm()           
    return render (request, 'login.html', {'form': form})

def registro(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'registro.html', {'form':form})    

class UserCreateView(CreateView):
    model = User
    success_url = reverse_lazy('login')
    template_name = 'registro.html'
    form_class = UserRegistrationForm

# Produce error method == si hay error en @login_required 
@login_required 
def editarPerfil(request):
    user1 = request.user

    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user1.email = data['email']
            user1.set_password(data['password1'])
            user1.set_password(data['password2'])
            user1.first_name = data['first_name']
            user1.last_name = data['last_name']
            user1.save()
            return redirect('login')
    else:
        form = UserEditForm({'email':user1.email})
    
    return render(request, 'registro.html', {'form':form})