from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    fecha_de_nacimiento = forms.DateField(
        required=True,
        label="Fecha de nacimiento",
        input_formats=['%Y-%m-%d'],
        help_text="Ingrese la fecha en formato AAAA-MM-DD",
        error_messages={
            'invalid': 'Ingrese la fecha en formato AAAA-MM-DD'
        }
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'fecha_de_nacimiento')

class CustomUserChangeForm(UserChangeForm):
    fecha_de_nacimiento = forms.DateField(
        required=True,
        label="Fecha de nacimiento",
        input_formats=['%Y-%m-%d'],
        help_text="Ingrese la fecha en formato AAAA-MM-DD",
        error_messages={
            'invalid': 'Ingrese la fecha en formato AAAA-MM-DD'
        }
    )

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'fecha_de_nacimiento')

class RegisterForm(CustomUserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True, label="Grupo de usuario")

    class Meta(CustomUserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'fecha_de_nacimiento', 'group')
