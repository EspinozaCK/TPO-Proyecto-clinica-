create database if not exists Turnos_Clinica;
use Turnos_Clinica;
CREATE TABLE IF NOT EXISTS turnos (
    id_paciente int auto_increment primary key,
    apellidoNombre varchar(100) not null,
    dni int unsigned not null,
    especialidad varchar(50),
    profesional varchar(30) not null,
    fecha date not null
    );
    alter table turnos
    modify especialidad enum ('Neurología','Odontología','Psicoloía','Dermatología','Podología','Ortodoncia','Pediatría','Cardiología','Ginecología') not null;
    alter table turnos
    modify especialidad enum ('Neurología','Odontología','Psicoloía','Dermatología','Podología','Ortopedia','Pediatría','Cardiología','Ginecología') not null ;
    alter table turnos
    modify especialidad varchar(50);