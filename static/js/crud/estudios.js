// Agregar valores al formulario de edición
function addValues(modal, titulo, institucion, fecha_inicio, fecha_fin, egresado){
    modal.querySelector('#titulo').value = titulo;
    modal.querySelector('#institucion').value = institucion;
    modal.querySelector('#fecha_inicio').value = fecha_inicio;
    modal.querySelector('#fecha_fin').value = fecha_fin;
    modal.querySelector('#egresado').value = egresado;
}

// Obtener los botones de editar
const editButtons = document.querySelectorAll('[data-formaction]');
// Obtener el modal
const modal = document.querySelector('#modal');
const closeButton = modal.querySelector('[data-modal-close]');

// Mostrar el modal al hacer clic en un botón de editar
editButtons.forEach(button => {
    button.addEventListener('click', () => {
        modal.showModal();
        // Agregar el formaction del botón al formulario del modal
        const formAction = button.dataset.formaction;
        const form = modal.querySelector('form');
        form.action = formAction;

        // Obtener los valores de los inputs del formulario
        const titulo = button.dataset.estudioTitulo;
        const institucion = button.dataset.estudioInstitucion;
        const fecha_inicio = button.dataset.estudioFechaInicio;
        const fecha_fin = button.dataset.estudioFechaFin;
        const egresado = button.dataset.estudioEgresadoId;
        console.log(egresado);

        // Agregar los valores al formulario del modal
        addValues(modal, titulo, institucion, fecha_inicio, fecha_fin, egresado);
    });
});

// Esconder el modal al hacer clic en el botón de cerrar
closeButton.addEventListener('click', () => {
    modal.close();
});