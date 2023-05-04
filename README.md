# 3erIndividual

Nombre de la aplicación: Helloworld_app

Objetivo de la aplicación: Helloworld_App es una aplicación web que permite a los usuarios autenticados acceder a diferentes funcionalidades y recursos en función de sus roles.

Funcionamiento de la aplicación:
1. Los usuarios pueden registrarse e iniciar sesión en la aplicación.
2. La aplicación muestra diferentes vistas y funcionalidades basadas en el rol del usuario.
3. Los usuarios pueden cerrar sesión en cualquier momento.

Restricciones de acceso:
1. Restricción basada en la autenticación: Solo los usuarios autenticados pueden acceder a ciertas vistas y funcionalidades. Se utiliza el decorador `@login_required` para aplicar esta restricción.
2. Restricción basada en roles: Los usuarios con roles específicos pueden acceder a ciertas vistas y funcionalidades. Se utiliza el decorador `@user_passes_test` junto con una función de prueba personalizada para aplicar esta restricción. En nuestro caso, solo los usuarios con el atributo `is_admin` pueden acceder a la vista `restricted_view`.

Personalización del inicio de sesión:
- Se ha personalizado la plantilla de inicio de sesión para mejorar la experiencia del usuario y adaptarla al estilo de la aplicación.
- Los mensajes de error se muestran si el inicio de sesión no es exitoso.

Mi Proyecto Django
==================

Este proyecto es una aplicación web desarrollada con Django que permite a los usuarios registrarse, iniciar sesión y acceder a diferentes áreas del sitio según su rol.

Grupos de usuarios
------------------

Hemos identificado dos grupos principales de usuarios en nuestra aplicación:

1. Usuarios regulares
2. Administradores

Características y permisos diferenciados
----------------------------------------

1. Usuarios regulares:
Los usuarios regulares son aquellos que utilizan la aplicación para realizar tareas básicas como ver contenido y publicar comentarios. Para este grupo de usuarios, hemos asignado los siguientes permisos:

- Ver contenido: Los usuarios regulares pueden ver el contenido publicado en la aplicación.
- Publicar comentarios: Los usuarios regulares pueden publicar comentarios en el contenido.

2. Administradores:
Los administradores son aquellos usuarios que tienen la responsabilidad de supervisar y gestionar la aplicación. Además de las funcionalidades disponibles para los usuarios regulares, los administradores tienen permisos adicionales para realizar acciones como:

- Crear, editar y eliminar contenido: Los administradores pueden crear, editar y eliminar contenido en la aplicación.
- Gestionar usuarios: Los administradores pueden ver, agregar, editar y eliminar usuarios en la aplicación.
- Gestionar comentarios: Los administradores pueden moderar y eliminar comentarios.

Razón para asignar permisos diferenciados
------------------------------------------

Hemos asignado permisos diferenciados a cada grupo de usuarios para asegurar una experiencia de usuario adecuada y un control eficiente de la aplicación.

Los usuarios regulares tienen permisos limitados para garantizar que puedan realizar las acciones básicas sin afectar la estructura y funcionalidad general de la aplicación.

Por otro lado, los administradores tienen permisos más amplios, lo que les permite gestionar la aplicación y asegurar su correcto funcionamiento. Al limitar los permisos de gestión a los administradores, se reduce el riesgo de acciones no autorizadas o malintencionadas que podrían dañar la aplicación.

