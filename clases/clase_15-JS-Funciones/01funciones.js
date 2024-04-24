
// Funcion basica

/*
Sintaxis
function name(params) {
    
}
*/


function saludar() {
    let res = 2 + 5
    document.write("Hola comision!!!", res)
}

saludar() // Invocacion de la funcion

function saludar2(nombre, a=0,b=3) {
    let res = a + b
    document.write("Hola comision!!! ",nombre, " ", res)
}

saludar2("Fernando",1,5) 

saludar2("Miriam",1,8) 
saludar2("Juli") 

function sumaLoca(a,b) {

    let res = a + b +5
    return res
    
}
// let res = 9
console.log(sumaLoca(2,6))

let suma= sumaLoca(4,7)

const pepe = 3.14
console.log(suma, pepe);

// pepe=56


// FUNCIONES QUE RETORNAN UN VALOR
function parseRatingToStars(rating){
    let response;
    rating = parseInt(rating)
    if(rating>10){
        return 'Este valor no corresponde';
    }
    rating = Math.round(rating/2)
    switch (rating) {
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


let ratingMovie="8"
let ratingMovieParsed = parseRatingToStars(ratingMovie)

console.log(ratingMovieParsed)
console.log(parseRatingToStars("4"))
console.log(parseRatingToStars("7.4"))
console.log(parseRatingToStars("22"))


// FUNCIONES FLECHA - ARROW FUNCTIONS
// con const, prevenimos que sea reasignada otro valor a la variable sellTicketFor

/*
() => {}

*/


const sellTicketFor = (numberTickets) => {
    for(i=0; i<numberTickets; i++) {
        console.log("Se vendio el ticket nro: ", i)
    }
    console.log("FIN de la VENTA")
}



sellTicketFor(3)

sellTicketFor(4)

// Callback, tipico en setTimeout

setTimeout(saludar, 5000)





