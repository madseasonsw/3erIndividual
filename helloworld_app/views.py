from django.shortcuts import render
from .models import CustomUser

def lista_de_usuarios(request):
    usuarios = CustomUser.objects.all()
    return render(request, 'lista_de_usuarios.html', {'usuarios': usuarios})

def landing_page(request):
    return render(request, 'landing.html')


