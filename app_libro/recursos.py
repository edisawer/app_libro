from flask_restful import Resource 
from flask import request 
from modelos import db, Book 
from auth import token_required

class LibroResource(Resource):
    @token_required
    def get(self, libro_id):
        libro = Book.query.get_or_404(libro_id)
        return libro.to_dict()

    @token_required
    def delete(self, libro_id):
        libro = Book.query.get_or_404(libro_id)
        db.session.delete(libro)
        db.session.commit()
        return '', 204

class ListaLibroResource(Resource):
    @token_required
    def get(self):
        autor = request.args.get('autor')
        genero = request.args.get('genero')
        query = Book.query

        if autor:
            query = query.filter(Book.autor == autor)
        if genero:
            query = query.filter(Book.genero == genero)

        libros = query.all()
        return [libro.to_dict() for libro in libros]

    @token_required
    def post(self):
        data = request.get_json()
        if 'titulo' not in data or 'autor' not in data:
            return {'error': 'Titulo y Autor son campos requeridos'}, 400
        nuevo_libro = Book(
            titulo=data['titulo'],
            autor=data['autor'],
            anio_publicacion=data.get('anio_publicacion'),
            genero=data.get('genero')
        )
        db.session.add(nuevo_libro)
        db.session.commit()
        return nuevo_libro.to_dict(), 201

    @token_required
    def put(self):
        data = request.get_json()
        libro = Book.query.get_or_404(data['id'])
        if 'titulo' in data:
            libro.titulo = data['titulo']
        if 'autor' in data:
            libro.autor = data['autor']
        if 'anio_publicacion' in data:
            libro.anio_publicacion = data['anio_publicacion']
        if 'genero' in data:
            libro.genero = data['genero']
        db.session.commit()
        return libro.to_dict(), 200
