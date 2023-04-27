from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
import uuid

def generate_unique_username():
    return str(uuid.uuid4())[:30]

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, nombre, fecha_de_nacimiento, password=None, **extra_fields):
        if not username:
            raise ValueError('El campo Username es obligatorio')
        if not email:
            raise ValueError('El campo Email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, nombre=nombre, fecha_de_nacimiento=fecha_de_nacimiento, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, nombre, fecha_de_nacimiento, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, nombre, fecha_de_nacimiento, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True, default=generate_unique_username)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_de_nacimiento = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nombre', 'email', 'fecha_de_nacimiento']

    def __str__(self):
        return self.nombre
