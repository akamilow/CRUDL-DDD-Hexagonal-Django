# CRUDL-DDD-Hexagonal-Django

Este proyecto implementa un CRUDL siguiendo los principios DDD y arquitectura Hexagonal usando Django.

## Pasos para correr el proyecto en otra máquina

1. Clona el repositorio:
   ```pwsh
   git clone https://github.com/akamilow/CRUDL-DDD-Hexagonal-Django.git
   cd CRUDL-DDD-Hexagonal-Django
   ```
2. Instala las dependencias:
   ```pwsh
   python -m venv venv
   venv\Scripts\activate
   ```
3. Realiza las migraciones:
   ```pwsh
   python manage.py migrate
   ```
4. Corre el servidor:
   ```pwsh
   python manage.py runserver
   ```

## Colección Postman

En la carpeta del proyecto se incluye una colección de Postman (`CRUDL-DDD-Hexagonal-Django.postman_collection.json`) para probar fácilmente los diferentes endpoints de la aplicación. Puedes importarla en Postman y ejecutar las peticiones de ejemplo para cada endpoint.