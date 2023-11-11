// Agregar valores al formulario de edición
function addValues(modal, egresadoId, sectorId){
    modal.querySelector('#egresado').value = egresadoId;
    modal.querySelector('#sector').value = sectorId;
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
        const egresadoId = button.dataset.sectorEgresadoEgresadoId;
        const sectorId = button.dataset.sectorEgresadoSectorId;

        // Agregar los valores al formulario del modal
        addValues(modal, egresadoId, sectorId);
    });
});

// Esconder el modal al hacer clic en el botón de cerrar
closeButton.addEventListener('click', () => {
    modal.close();
});