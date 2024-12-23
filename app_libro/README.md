# API REST de Gestión de Libros

## Instalación

## bash
pip install Flask Flask-RESTful Flask-SQLAlchemy

python init_db.py

$env:FLASK_APP="app.py"			# windows
# export FLASK_APP=app.py 		# linux

flask run

# USO DE ENDPOINTS

## BASE URL

http://localhost:5000

# 1. Crear un Libro

URL: /LIBROS

Método: POST

Encabezados:

Content-Type: application/json

x-access-token:  

#Formato de parametros a enviar json.

{
  "titulo": "Libro 2",
  "autor": "Autor 2",
  "anio_publicacion": 2024,
  "genero": "Terror"
}


# 2. Listar Todos los Libros

URL: /libros

Método: GET

Encabezados:

x-access-token: mitokensecreto

Parámetros de Consulta:

autor (opcional): Filtra por autor

genero (opcional): Filtra por genero



# 3. Ver Detalles de un Libro

URL: /libros/libro_id

Método: GET

Encabezados:

x-access-token: mitokensecreto



# 4. Actualizar un Libro

URL: /libros

Método: PUT

Encabezados:

Content-Type: application/json

x-access-token: mitokensecreto

{  
  "id": 2,
  "titulo": "Libro 2",
  "autor": "Autor 2",
  "anio_publicacion": 2024,
  "genero": "Terror"
}



# 5. Eliminar un Libro

URL: /libros/libro_id

Método: DELETE

Encabezados:

x-access-token: mitokensecreto
