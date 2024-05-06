// Función asincrónica para cargar y mostrar los datos
async function cargarYMostrarDatos() {
    try {
        // Hacer la solicitud HTTP para obtener el archivo JSON
        const response = await fetch('./movies.json');
        
        // Verificar si la solicitud fue exitosa
        if (!response.ok) {
            throw new Error('Error al leer el archivo JSON');
        }
        
        // Convertir la respuesta JSON en un objeto JavaScript
        const datos = await response.json();
        
        // Mostrar los datos en la página HTML
        mostrarDatos(datos.results);
    } catch (error) {
        // Capturar y manejar cualquier error que ocurra durante el proceso
        console.error(error);
    }
}

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

// Llamar a la función principal para cargar y mostrar los datos cuando el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', cargarYMostrarDatos);
