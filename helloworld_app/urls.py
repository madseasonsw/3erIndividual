from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('usuario/', views.lista_de_usuarios, name='lista_de_usuarios'),
    path('register/', views.register, name='register'),
    # ... otras rutas ...
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

