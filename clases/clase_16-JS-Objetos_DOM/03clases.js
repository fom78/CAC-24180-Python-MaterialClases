/*
- Las clases en proporcionan una forma de crear objetos con un conjunto predefinido de propiedades y métodos.
- Las clases son una forma de definir un tipo de objeto en JavaScript, siguiendo el paradigma de la programación orientada a objetos (POO).
- Se definen utilizando la palabra clave class.
- Las clases pueden tener un constructor para inicializar las propiedades del objeto cuando se crea una nueva instancia de la clase.

*/

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

let movie2 = new Movie('El señor de los anillos 2',7.3,120,"Release")
movie2.viewGeneralResume()

let movie3 = new Movie('Batman',8.5,98)

console.log(">>>>>>>>>>💚❤️",typeof(movie3))
movie3.viewGeneralResume()

console.log(movie2);

