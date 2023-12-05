from flask import Flask, request, jsonify
from flask_cors import CORS  
import mysql.connector

app = Flask(__name__)
CORS(app)


config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'Turnos_Clinica',
    'raise_on_warnings': True
}

@app.route('/guardar-turno', methods=['POST'])
def guardar_turno():
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        
        data = request.get_json()

        
        cursor.execute("INSERT INTO turnos (apellidoNombre, dni, especialidad, profesional, fecha) VALUES (%s, %s, %s, %s, %s)",
                       (data['apellidoNombre'], data['dni'], data['especialidad'], data['profesional'], data['fecha']))

        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({"mensaje": "Turno guardado exitosamente"})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
