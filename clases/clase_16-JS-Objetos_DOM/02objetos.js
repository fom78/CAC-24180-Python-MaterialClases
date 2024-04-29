let movie = {
    title:'El señor de los anillos 3',
    vote_average: 9.5,
    runtime: 90,
    status: 'Released',
    play: function(){
        console.log('Reproduciendo la pelicula');
    },
    stop: function(){
        console.log('Deteniendo la reproduccion');
    },
    viewGeneralResume: function(){
        console.log('Titulo: ',this.title);
        console.log('duracion: ',this.runtime);
        console.log('Estado: ',this.status);
    }
}

// console.log(typeof(movie));
// movie.viewGeneralResume();
movie.play()

movie.title='El señor de los anillos 2'
console.log(movie.title)
// console.log(movie.title);
movie.year=2003
console.log(movie.year);
// movie.play();
// movie.stop();
// movie.viewCredits();

// console.log(movie);

// movie.reparto = 'çualquiera';
// console.log(movie.reparto);


let movie2 = {
    title:'El señor de los anillos 4',
    vote_average: 7.5,
    runtime: 90,
    status: 'Released',
    adult: true,
    play: function(){
        console.log('Reproduciendo la pelicula');
    },
    stop: function(){
        console.log('Deteniendo la reproduccion');
    },
    viewGeneralResume: function(){
        console.log('Titulo: ',this.title);
        console.log('duracion: ',this.runtime);
        console.log('Estado: ',this.status);
    }
}

