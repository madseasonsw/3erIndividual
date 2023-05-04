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
