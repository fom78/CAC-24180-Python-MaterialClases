// El objeto localStorage proporciona una forma sencilla de almacenar datos en el navegador web.

// Almacenar datos en localStorage
localStorage.setItem('nombre', 'Juan');
localStorage.setItem('edad', '30');

// Obtener datos de localStorage
const nombre = localStorage.getItem('nombre');
const edad = localStorage.getItem('edad');

console.log(nombre); // Salida: Juan
console.log(edad);   // Salida: 30

// Eliminar un elemento de localStorage
localStorage.removeItem('nombre');

// Borrar todos los elementos de localStorage
localStorage.clear();
