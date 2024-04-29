// La función addEventListener permite agregar un "escuchador" a un elemento HTML
// para detectar eventos y ejecutar una función cuando ocurre ese evento.

// Ejemplo de uso de addEventListener para detectar un clic en un botón:
const boton = document.getElementById('mi-boton')
boton.addEventListener('click', function() {
    console.log('Se hizo clic en el botón')
    viewMovie()
})

// También puedes pasar una función de "callback" definida previamente como argumento:
/*
function clicHandler() {
    console.log('Se hizo clic en el botón')
}

boton.addEventListener('click', clicHandler)
// Para quitar un "escuchador" previamente agregado, puedes utilizar removeEventListener:
boton.removeEventListener('click', clicHandler)
*/

// Otros eventos comunes incluyen 'mouseover' (pasar el ratón por encima), 'mouseout' (sacar el ratón de encima),
// 'input' (cambios en un campo de entrada), 'change' (cambios en un campo de selección), etc.

// También puedes utilizar eventos de teclado, como 'keydown', 'keyup', y 'keypress' para detectar pulsaciones de teclas.

