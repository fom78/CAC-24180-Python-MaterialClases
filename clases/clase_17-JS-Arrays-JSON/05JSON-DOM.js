// Esperar a que el DOM esté completamente cargado antes de ejecutar el código
document.addEventListener('DOMContentLoaded', function() {
    // Hacer la solicitud HTTP para obtener el archivo JSON
    fetch('./movies.json')
        .then(response => {
            // Verificar si la solicitud fue exitosa
            if (!response.ok) {
                // Lanzar un error si la solicitud no fue exitosa
                throw new Error('Error al leer el archivo JSON');
            }
            // Convertir la respuesta JSON en un objeto JavaScript
            return response.json();
        })
        .then(datos => {
            // Una vez que los datos se han obtenido correctamente,
            // llamar a la función mostrarDatos para mostrarlos en la página HTML
            mostrarDatos(datos.results);
        })
        .catch(error => {
            // Capturar y manejar cualquier error que ocurra durante el proceso
            console.error(error);
        });
});

// Función para mostrar los datos en la página HTML
function mostrarDatos(datos) {
    // Encontrar el elemento en el DOM con el id 'resultado'
    const resultado = document.querySelector('#resultado');
    // Iterar a través de los datos recibidos
    for (let i = 0; i < datos.length; i++) {
        // Crear un fragmento de HTML para cada conjunto de datos
        let elementoHTML =  `<div>
            <p>Nombre: ${datos[i].title}</p>
            <p>Edad: ${datos[i].vote_average}</p>
            <p>Ciudad: ${datos[i].poster_path}</p>
        </div>`;
        // Agregar el fragmento HTML al final del elemento 'resultado' en el DOM
        resultado.insertAdjacentHTML('beforeend', elementoHTML);
    }
}

// Utilizando forEach():
/*

function mostrarDatos(datos) {
    const resultado = document.querySelector('#resultado');
    // Utilizando forEach para iterar sobre cada elemento del array
    datos.forEach(dato => {
        // Crear un fragmento de HTML para cada conjunto de datos
        let elementoHTML =  `<div>
            <p>Nombre: ${dato.title}</p>
            <p>Edad: ${dato.vote_average}</p>
            <p>Ciudad: ${dato.poster_path}</p>
        </div>`;
        // Agregar el fragmento HTML al final del elemento 'resultado' en el DOM
        resultado.insertAdjacentHTML('beforeend', elementoHTML);
    });
}

*/

// Utilizando map():

/*
function mostrarDatos(datos) {
    const resultado = document.querySelector('#resultado');
    // Utilizando map para crear un nuevo array con los fragmentos de HTML
    const elementosHTML = datos.map(dato => {
        return `<div>
            <p>Nombre: ${dato.title}</p>
            <p>Edad: ${dato.vote_average}</p>
            <p>Ciudad: ${dato.poster_path}</p>
        </div>`;
    });
    // Unir los fragmentos de HTML en una sola cadena
    const contenidoHTML = elementosHTML.join('');
    // Agregar el contenido HTML al final del elemento 'resultado' en el DOM
    resultado.insertAdjacentHTML('beforeend', contenidoHTML);
}


*/