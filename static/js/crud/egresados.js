// Agregar valores al formulario de edición
function addValues(modal, input, fechaNacimiento, nivelEducativo, salario, experienciaMeses, ciudad){
    modal.querySelector('#fecha_nacimiento').value = fechaNacimiento;
    modal.querySelector('#nivel_educativo').value = nivelEducativo;
    modal.querySelector('#salario').value = salario.replace(',', '.');
    modal.querySelector('#experiencia_meses').value = experienciaMeses;
    modal.querySelector('#ciudad').value = ciudad;
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
        const fechaNacimiento = button.dataset.egresadoFechaNacimiento;
        const nivelEducativo = button.dataset.egresadoNivelEducativo;
        const salario = button.dataset.egresadoSalario;
        const experienciaMeses = button.dataset.egresadoExperienciaMeses;
        const ciudad = button.dataset.egresadoCiudad;

        // Agregar los valores al formulario del modal
        addValues(modal, form, fechaNacimiento, nivelEducativo, salario, experienciaMeses, ciudad);
    });
});

// Esconder el modal al hacer clic en el botón de cerrar
closeButton.addEventListener('click', () => {
    modal.close();
});