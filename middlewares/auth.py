from flask import request, jsonify
from decouple import config

API_KEY = config('API_KEY')  # Carga la clave API desde .env

def requiere_api_key(func):
    def wrapper(*args, **kwargs):
        api_key = request.headers.get('x-api-key')
        if not api_key or api_key != API_KEY:
            return jsonify({'error': 'No autorizado'}), 401
        return func(*args, **kwargs)
    return wrapper
