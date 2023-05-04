from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('usuario/', views.lista_de_usuarios, name='lista_de_usuarios'),
    path('register/', views.register, name='register'),
     path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('after_login/', views.after_login, name='after_login'),
    path('restricted/', views.restricted_view, name='restricted_view'),
    # ... otras rutas ...
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

