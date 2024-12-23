from functools import wraps
from flask import request, jsonify

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')
        if not token:
            return jsonify({'message': 'Token no encontrado!'}), 401
        if token != 'mitokensecreto':
            return jsonify({'message': 'Token invalido!'}), 401
        return f(*args, **kwargs)
    return decorated
