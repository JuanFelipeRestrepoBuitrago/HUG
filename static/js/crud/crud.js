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

// .caret {
//     border-left: 4px solid transparent;
//     border-right: 4px solid transparent;
//     border-top: 5px solid var(--black);
//     position: absolute;
//     right: 10px;
//     top: 65%;
//     width: 0;
//     height: 0;
//     transition: 0.3s;
// }
//
// .caret-rotate {
//     transform: rotate(180deg);
// }