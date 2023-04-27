from django.shortcuts import render
from .models import CustomUser
from django.contrib.auth import login
from .forms import RegisterForm
from django.shortcuts import render, redirect


def lista_de_usuarios(request):
    usuarios = CustomUser.objects.all()
    return render(request, 'lista_de_usuarios.html', {'usuarios': usuarios})

def landing_page(request):
    return render(request, 'landing.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('landing_page')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def save_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Crear un nuevo objeto CustomUser y guardar los datos del formulario en la base de datos
        new_user = CustomUser(first_name=first_name, last_name=last_name, email=email)
        new_user.set_password(password)
        new_user.save()
        
        return redirect('home') # Reemplaza 'home' con la vista a la que deseas redirigir después de guardar los datos
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})