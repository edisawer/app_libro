from flask import Flask
from flask_restful import Api
from modelos import db
from recursos import LibroResource, ListaLibroResource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///libros.db'

db.init_app(app)
api = Api(app)

@app.before_request
def create_tables():
    db.create_all()

api.add_resource(LibroResource, '/libros/<int:libro_id>')
api.add_resource(ListaLibroResource, '/libros')

if __name__ == '__main__':
    app.run(debug=True)

