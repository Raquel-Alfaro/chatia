
# Entrega convocatoria mayo

CHAT IA - Proyecto Final 2025/2026

Aplicacion web tipo chat asistente-IA desarrollada con Python, Django, HTML y Bootstrap.

## Datos
* Nombre: Raquel Alfaro Kerguelen
* Titulación: Ing. Sistemas de Telecomunicacion
* Cuenta en laboratorios: ralfaro
* Cuenta URJC: r.alfaro.2017@alumnos.urjc.es
* Vídeo (URL): https://youtu.be/bxsqWyaZ3I4
* Despliegue (URL): https://django-chatia.onrender.com
* Usuarios y contraseñas: user1/contraseña1
* Cuenta Admin Site: admin/1234admin

## Recursos y métodos HTTP
* Recurso: /
* Métodos permitidos: GET

* Recurso: /login/
* Métodos permitidos: GET, POST

* Recurso: /logout/
* Métodos permitidos: POST

* Recurso: /conversation/new/
* Métodos permitidos: POST

* Recurso: /chat/<conversation_id>/
* Métodos permitidos: GET, POST

* Recurso: /rename/<conversation_id>/
* Métodos permitidos: POST

* Recurso: /delete/<conversation_id>/
* Métodos permitidos: POST

* Recurso: /profile/
* Métodos permitidos: GET, POST

* Recurso: /help/
* Métodos permitidos: GET

* Recurso: /admin/
* Métodos permitidos: GET, POST


## Resumen parte obligatoria
La práctica consiste en una aplicación web en la que se puede mantener una 
conversacion con una IA, desarrollada con Django y SQLite3.

La aplicacion permite a cada usuario logeado crear conversaciones, enviar
prompts a un modelo LLM real y recibir respuestas.

La aplicacion tiene:
- Admin Site para administrar los datos

- Sistema de autenticacion de usuarios
- Historial de conversaciones
- Gestion de las conversaiones (crear, acceder, renombrar y borrar) 
- Gestion del perfil de usuario (alias y tema)
- Confirmacion antes de borrar una conversacion
- Navegacion entre paginas principales (home, chat, perfil y ayuda)

- Las conversaciones estan asociadas al usuario
- Integracion real con una API LLM
- Diseño responsive (por uso de Bootstrap)
- Separacion de mensajes de usuario y asistente
- Scroll automatico al ultimo mensaje
- Estructura modular basada en modelos (Conversation, Message, Profile)

Tecnologias usadas para el desarrollo de la aplicacion-web:
-- Frontend:
- HTML5
- HTMX
- Bootstrap
- CSS3
-- Backend:
- Python 3
- Django
- SQLite3

## Lista partes opcionales
* Renombrar conversaciones: nos permite cambiar el nombre a una conversacion.

* Interfaz responsive moderna: por el uso de Bootstrap.

* Actualización dinámica mediante HTMX: se recargan los mensajes y el contenido de la conversacion
sin regarcar la pagina completa.

* Mejoras experiencia de usuario: scroll automático al último mensaje, confirmación antes de 
borrar conversaciones y los mensajes del usuario y la IA estan separados.

* Gestiones extra sobre conversaciones: se pueden eliminar y renombrar sin afectar al resto.

* Perfil de usuario: cada usuario puede elegir el alias con el que se nombrara en las conversaciones.
