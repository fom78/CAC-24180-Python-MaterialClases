/* 
OPERADORES RELACIONALES O DE COMPARACION

== igual a
=== igual valor y tipo
!= no igual a
!== igual valor no tipo
> mayor que
< menor que
>= mayor o igual que
<= menor o igual que
? operador ternario

*/


/*
OPERADORES LOGICOS
&& Y lógico (Conjunción)
|| O lógico (Disyunción)
! NO lógico (Negación)

*/

var1 = true && false
var2= false || true 

var3 = !var2

/*
JERARQUIA DE OPERADORES

*/

// RESOLVER 
resultado = true && 6+6 < 2-1*5 || 5*8 == "40" && !false

//  t Y 12 < 2-5  O  40 == "40" Y t

// t Y 12 < -3 O t Y t

// t Y f O t

// f O t ......>>>> true

console.log("El res es: ",resultado)
