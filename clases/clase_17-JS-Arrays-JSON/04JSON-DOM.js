/*
La asincronía en JavaScript se refiere a la capacidad del lenguaje para realizar operaciones sin bloquear la ejecución del código. En términos simples, significa que JavaScript puede ejecutar múltiples tareas simultáneamente sin tener que esperar a que una tarea se complete antes de comenzar otra. Esto es fundamental para trabajar con operaciones que pueden llevar tiempo, como la obtención de datos de una API, la carga de archivos o la ejecución de operaciones de red

¿Cómo gestionar la asincronía?En JavaScript, la asincronía se maneja principalmente utilizando callbacks, promesas y async/await.
- Callbacks: Es una función que se pasa como argumento a otra función y se invoca después de que alguna operación asíncrona se completa. Sin embargo, el anidamiento excesivo de callbacks puede llevar a lo que se conoce como "callback hell" o "infierno de callbacks", lo que dificulta la legibilidad y el mantenimiento del código.
- Promesas: Las promesas en JavaScript son objetos que representan el resultado eventual (éxito o fracaso) de una operación asíncrona. Una promesa puede estar en uno de los siguientes estados:
    - Pendiente: Estado inicial, antes de que se resuelva o se rechace la promesa.
    - Resuelta: La operación asíncrona se completó exitosamente y la promesa se resuelve con un valor.
    - Rechazada: La operación asíncrona falló y la promesa se rechaza con un motivo o error.
Las promesas tienen métodos como then() y catch() que permiten encadenar acciones a realizar cuando la promesa se resuelve o se rechaza respectivamente, lo que proporciona un código más limpio y legible para manejar operaciones asíncronas. Además, las promesas pueden encadenarse utilizando el método then() para manejar múltiples operaciones asíncronas de manera secuencial.
- async/await: Es una sintaxis que permite escribir código asíncrono de manera más sincrónica. Las funciones marcadas con async devuelven automáticamente una promesa, y el operador await pausa la ejecución de la función hasta que la promesa se resuelva o rechace, lo que hace que el código sea más fácil de leer y entender.
### FETCH ###
fetch es una función incorporada en los navegadores modernos que permite hacer solicitudes HTTP desde el cliente hacia un servidor y manejar las respuestas de manera asíncrona. Esta API proporciona una interfaz más moderna y flexible en comparación con las técnicas anteriores como XMLHttpRequest (XHR). 
fetch devuelve una promesa que eventualmente se resolverá con el objeto Response representando la respuesta a la solicitud HTTP.
*/

// Hacer la solicitud HTTP para obtener el archivo JSON
const var1 = fetch('./data.json')
    .then(response => {
        // Verificar si la solicitud fue exitosa
        if (!response.ok) {
            // Lanzar un error si la solicitud no fue exitosa
            throw new Error('Error al leer el archivo JSON')
        }
        console.log("❤️ 1")
        // Convertir la respuesta JSON en un objeto JavaScript
        return response.json() // Da una promesa

    })
    .then(datos => {
        // Una vez que los datos se obtienen con éxito, llamar a la función mostrarDatos
        console.log("❤️ 3")
        mostrarDatos(datos)
    })
    .catch(error => {
        // Capturar y manejar cualquier error que ocurra durante el proceso
        console.error(error)
    })


// Función para mostrar los datos en la página HTML
function mostrarDatos(datos) {
    // Obtener el elemento con id 'resultado'
    const resultado = document.getElementById('resultado')
    // Insertar los datos obtenidos del archivo JSON en el elemento resultado
    resultado.innerHTML = `
        <p>Nombre: ${datos.nombre}</p>
        <p>Edad: ${datos.edad}</p>
        <p>Ciudad: ${datos.ciudad}</p>
    `
}

console.log("❤️ 4")

const suma = 3+6

console.log(">>>>",var1);
