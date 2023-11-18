from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('turnero.html')

@app.route('/guardar_turno', methods=['POST'])
def guardar_turno():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        dni = request.form['dni']
        telefono = request.form['telefono']
        dia = request.form['dia']
        hora = request.form['hora']

        # Aquí puedes realizar la lógica para almacenar los datos en una base de datos o hacer lo que necesites
        # Por ahora, solo imprimiremos los datos para demostrar que se recibieron correctamente
        print(f'Turno agendado para {nombre} {apellido}.')
        print(f'DNI: {dni}')
        print(f'Teléfono: {telefono}')
        print(f'Fecha: {dia}')
        print(f'Hora: {hora}')

        return 'Turno agendado correctamente.'

if __name__ == '__main__':
    app.run(debug=True)
