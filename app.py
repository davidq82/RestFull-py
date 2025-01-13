from flask import Flask, jsonify, request
from services.zonas_service import obtener_zonas, agregar_zona, editar_zona, eliminar_zona
from middlewares.auth import requiere_api_key

app = Flask(__name__)

@app.route('/zonas', methods=['GET'])
@requiere_api_key
def listar_zonas():
    zonas = obtener_zonas()
    return jsonify(zonas)

@app.route('/zonas', methods=['POST'], endpoint='crear_zona')
@requiere_api_key
def crear_zona():
    data = request.json
    nombre = data.get('nombre')
    if not nombre:
        return jsonify({'error': 'El campo "nombre" es requerido'}), 400
    resultado = agregar_zona(nombre)
    return jsonify(resultado)

@app.route('/zonas/<int:id>', methods=['PUT'], endpoint='actualizar_zona')
@requiere_api_key
def actualizar_zona(id):
    data = request.json
    nombre = data.get('nombre')
    if not nombre:
        return jsonify({'error': 'El campo "nombre" es requerido'}), 400
    resultado = editar_zona(id, nombre)
    return jsonify(resultado)

@app.route('/zonas/<int:id>', methods=['DELETE'], endpoint='borrar_zona')
@requiere_api_key
def borrar_zona(id):
    resultado = eliminar_zona(id)
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)
