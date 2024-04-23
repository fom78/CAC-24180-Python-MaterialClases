/**
 * IF ELSE ELSE IF
 * 
 * if (condicion) {
 * codigo
 * }
 */

let var1 = !(3 == 4)

if (var1) {
    console.log("Hola")
    document.write("Hola que tal")
}


edad = prompt("Dame tu edad: ") // da un str

edad =  parseInt(edad) // "10"  sale un 10

// if (edad >= 18 ) {
//     document.write("Sos mayor podes ingresar a la fiesta") 
// } else {
//     document.write("Sos menor NO podes ingresar a la fiesta") 

// }

if (edad >= 45 ) {
    document.write("Categoria Senior") 
} 
else if (edad > 23) {
    document.write("Categoria Cadete") 
} 
else if (edad > 19) {
    document.write("Categoria Sub 23") 
} else if (edad === 10) {
    document.write("Categoria escuelita") 
} else {
    document.write("No se quien sos!!!") 

}

let altura = "1.45"
altura = parseFloat(altura)

/**
 * SWITCH
 * switch (variableAEvaluar) {
 *  case valor1:
 *      codigo
 *      break
 *  case valor2:
 *      codigo
 *      break
 *  case valorn:
 *      codigo
 *      break
 * default:
 *  codigo
 * break
 * }
 */

document.write("<br>") 

switch (edad) {
      case 10:
        document.write("ten") 
          break
      case 14:
        document.write("catorce") 
          break
      case 18:
        document.write("mayor") 
          break
     default:
        document.write("no tenes ni 10, ni 14 ni 18") 

     break
     }

document.write("<br>FINAL") 


