


// Busca en el documento HTML un elemento con el id 'movie-detail' y lo guarda en la variable 'div'
let div = document.querySelector('#movie-detail')

// Crea una nueva instancia de la clase 'Movie' con título, calificación, duración y estado
let movie = new Movie('El señor de los anillos 2', 7.3, 120, "Release")

// Define un bloque de texto HTML que mostrará la información de la película
let html = `
    <p>Titulo:${movie.title}</p> 
    <p>Duración:${movie.runtime}</p> 
    <p>estado:${movie.status}</p> 
`
let html2 = `
    <p>Titulo:OTRA</p> 
    <p>Duración:${movie.runtime}</p> 
    <p>estado:${movie.status}</p> 
`
// Inserta el bloque de texto HTML dentro del elemento 'div' al final de su contenido
div.insertAdjacentHTML('beforeend', html)




const viewMovie = () => {
    let div = document.querySelector('#movie-detail')
    // console.log(typeof(div),">>>>> ", div)
    let movie = new Movie('El señor de los anillos 2',7.3,120,"Release")
    let html = `
         <p>Titulo:${movie.title}</p>
         <p>Duracion:${movie.runtime}</p>
         <p>estado:${movie.status}</p>
     `
    div.insertAdjacentHTML('beforeend',html)
}
