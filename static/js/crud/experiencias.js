// Agregar valores al formulario de edición
function addValues(modal, empresa, cargo, fecha_inicio, fecha_fin, egresado){
    modal.querySelector('#empresa').value = empresa;
    modal.querySelector('#cargo').value = cargo;
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
        const empresa = button.dataset.experienciaEmpresa;
        const cargo = button.dataset.experienciaCargo;
        const fecha_inicio = button.dataset.experienciaFechaInicio;
        const fecha_fin = button.dataset.experienciaFechaFin;
        const egresado = button.dataset.experienciaEgresadoId;

        // Agregar los valores al formulario del modal
        addValues(modal, empresa, cargo, fecha_inicio, fecha_fin, egresado);
    });
});

// Esconder el modal al hacer clic en el botón de cerrar
closeButton.addEventListener('click', () => {
    modal.close();
});