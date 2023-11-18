function agendarTurno() {
    // Obtener los valores del formulario
    const nombre = document.getElementById('nombre').value;
    const apellido = document.getElementById('apellido').value;
    const dni = document.getElementById('dni').value;
    const telefono = document.getElementById('telefono').value;
    const dia = document.getElementById('dia').value;
    const hora = document.getElementById('hora').value;

    // Validar que todos los campos estén completos
    if (!nombre || !apellido || !dni || !telefono || !dia || !hora) {
        alert('Por favor, complete todos los campos.');
        return;
    }

    // Crear un mensaje de confirmación
    const confirmacion = `Turno agendado para ${nombre} ${apellido}.\nDNI: ${dni}\nTeléfono: ${telefono}\nFecha: ${dia}\nHora: ${hora}`;

    // Mostrar el mensaje de confirmación
    document.getElementById('confirmacion').innerText = confirmacion;
}
