
class Movie{
    constructor(title, mediaVotos, duracion=5,estado="Prep"){
        this.title=title
        this.vote_average=mediaVotos
        this.runtime=duracion
        this.status= estado        
    }

    play(){
        console.log('Reproduciendo la pelicula')
    }

    stop(){
        console.log('Deteniendo la reproduccion');
    }

    viewGeneralResume(){
        console.log('Titulo: ',this.title)
        console.log('duración: ',this.runtime)
        console.log('Estado: ',this.status)
    }
}

// Busca en el documento HTML un elemento con el id 'movie-detail' y lo guarda en la variable 'div'
let detalle = document.querySelector('#movie-detail')

console.log(detalle);

// Crea una nueva instancia de la clase 'Movie' con título, calificación, duración y estado
let movie = new Movie('El señor de los anillos 2', 7.3, 120, "Release")

// Define un bloque de texto HTML que mostrará la información de la película
let html = `
    <p>Titulo:${movie.title}</p> 
    <p>Duración:${movie.runtime}</p> 
    <p>estado:${movie.status}</p> 
`
console.log("❤️",html);
let html2 = `
    <p>Titulo:OTRA</p> 
    <p>Duración:58888</p> 
    <p>estado:nada</p> 
`
// Inserta el bloque de texto HTML dentro del elemento 'div' al final de su contenido
detalle.insertAdjacentHTML('beforeend', html)
detalle.insertAdjacentHTML('beforeend', html2)
detalle.insertAdjacentHTML('beforeend', html)



// const viewMovie = () => {
//     let div = document.querySelector('#movie-detail')
//     // console.log(typeof(div),">>>>> ", div)
//     let movie = new Movie('El señor de los anillos 2',7.3,120,"Release")
//     let html = `
//          <p>Titulo:${movie.title}</p>
//          <p>Duracion:${movie.runtime}</p>
//          <p>estado:${movie.status}</p>
//      `
//     div.insertAdjacentHTML('beforeend',html)
// }
