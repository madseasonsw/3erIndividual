from django.contrib import admin
from django.urls import path, include
from helloworld_app.views import register


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('', include('helloworld_app.urls')),
  

]


