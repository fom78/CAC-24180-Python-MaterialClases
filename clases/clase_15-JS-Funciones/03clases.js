/*
- Las clases en proporcionan una forma de crear objetos con un conjunto predefinido de propiedades y métodos.
- Las clases son una forma de definir un tipo de objeto en JavaScript, siguiendo el paradigma de la programación orientada a objetos (POO).
- Se definen utilizando la palabra clave class.
- Las clases pueden tener un constructor para inicializar las propiedades del objeto cuando se crea una nueva instancia de la clase.

*/

class Movie {
        constructor(name, status,vote_average) {
            this.name = name;
            this.status = status;
            this.vote_average = vote_average;
        }
    
        ratingInStars (rating){
            let response;
            if(rating>10){
                return 'Este valor no corresponde';
            }
            switch (parseInt(rating)) {
                case 5:
                    response = '⭐⭐⭐⭐⭐';
                    break;
                case 4:
                    response = '⭐⭐⭐⭐';
                    break;
                case 3:
                    response = '⭐⭐⭐';
                    break;
                case 2:
                    response = '⭐⭐';
                    break;
                case 1:
                    response = '⭐';
                    break;
                default:
                    response = '---';
                    break;
            }
            return response;    
        }
    }
    
    //let movie2 = new Movie('Titanic', "Release", 8.89);
    