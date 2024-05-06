/*
JSON (JavaScript Object Notation) es un formato de intercambio de datos liviano y fácil de leer que se utiliza para transferir datos entre un servidor y un cliente web, y también para el almacenamiento de datos
*/

class Movie {
    constructor(titulo, mediaVotos, duracion, estado = "Prep") {
        this.title = titulo;
        this.vote_average = mediaVotos;
        this.runtime = duracion;
        this.status = estado;
    }

    // Métodos adicionales de la clase Movie
    play() {
        console.log('Reproduciendo la película');
    }

    stop() {
        console.log('Deteniendo la reproducción');
    }

    viewGeneralResume() {
        console.log('Título:', this.title);
        console.log('Duración:', this.runtime);
        console.log('Estado:', this.status);
    }
}

// Crear una instancia de la clase Movie
let movie2 = new Movie('El señor de los anillos 2', 7.3, 120, "Release");

// Convertir objeto Movie a JSON usando JSON.stringify()
const movieJSON = JSON.stringify(movie2);
console.log("movieJSON",movieJSON, typeof(movieJSON));
// Salida (un string): {"title":"El señor de los anillos 2","vote_average":7.3,"runtime":120,"status":"Release"}

// Convertir JSON a objeto Movie usando JSON.parse()
const movieObjeto = JSON.parse(movieJSON);
console.log("movieObjeto",movieObjeto, typeof(movieObjeto));
// Salida(un objeto): { title: 'El señor de los anillos 2', vote_average: 7.3, runtime: 120, status: 'Release' }


