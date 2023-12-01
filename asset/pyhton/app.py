from flask import Flask, render_template, request
import mysql.connector
from flaskext.mysql import MySQL
app = Flask(__name__)

mysql= MySQL()

import mysql.connector
from flask import _request_ctx_stack

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Turnos_Clinica"
)


cursor = conexion.cursor()


try:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS turnos (
            id_paciente int auto_increment primary key,
            apellidoNombre varchar(100) not null,
            dni int unsigned not null,
            especialidad especialidad enum ('Neurología','Odontología','Psicoloía','Dermatología','Podología','Ortopedia','Pediatría','Cardiología','Ginecología') not null,
            profesional varchar(30) not null,
            fecha date not null
        )
    """)
    
    cursor.execute("""
        ALTER TABLE turnos
        MODIFY especialidad enum (
            'Neurología', 'Odontología', 'Psicología', 'Dermatología',
            'Podología', 'Ortopedia', 'Pediatría', 'Cardiología', 'Ginecología'
        ) not null
    """)
    
    conexion.commit()
    
    print("Base de datos configurada correctamente.")
    
except mysql.connector.Error as err:
    print(f"Error: {err}")
    
    conexion.rollback()
    
finally:
    
    cursor.close()
    conexion.close()