from flask import Flask, jsonify
from flask import request
import os

app = Flask(__name__)

# Ruta para el endpoint principal del API
@app.route('/api/v1/hola', methods=['GET'])
def hola():
    mensaje = {'mensaje': 'Hola, mundo!'}
    return jsonify(mensaje)

# Punto de entrada del programa
if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))