// Obtener la flecha de la lista desplegable
const caret = document.querySelector('.caret');
// Obtener el select
const select = document.querySelector('#nivel_educativo');

// Rotar la flecha de la lista desplegable al hacer clic en ella
select.addEventListener('mousedown', () => {
    caret.classList.toggle('caret-rotate');
});

// Esconder la flecha de la lista desplegable al hacer clic fuera de ella
document.addEventListener("click", function (event) {
    if (!select.contains(event.target) || event.target === caret) {
        caret.classList.remove('caret-rotate');
    }
});

// Esconder la flecha de la lista desplegable al seleccionar una opción
select.addEventListener('change', () => {
    caret.classList.remove('caret-rotate');
});

// Obtener los botones de editar
const editButtons = document.querySelectorAll('[data-formaction]');
// Obtener el modal
const modal = document.querySelector('#modal');

// Mostrar el modal al hacer clic en un botón de editar
editButtons.forEach(button => {
    button.addEventListener('click', () => {
        modal.showModal();
    });
});