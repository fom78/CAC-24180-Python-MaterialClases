# Iterativas: sentencia while y for
# Las sentencias iterativas se utilizan para repetir un bloque de código varias veces.

# Sentencia while
# Se ejecuta mientras una condición sea verdadera.

contador = 0
while contador < 5:
    print("El contador es:", contador)

    contador = contador + 1
# continuar = "H"
# while continuar != "n":
    
#     2+9
#     print("Algo")
#     continuar = input("Desea continuar (s/n) ? ")

# while contador < 5:
#     4+9
#     while True:
        
#         2+9
#         print("Algo")
#         continuar = input("Desea continuar (s/n) ? ")
#         if continuar == "n":
#             break
#     print("Fuera del while True")
#     contador = contador + 1


# Sentencia for
# Se utiliza para iterar sobre una secuencia (por ejemplo, una lista o una cadena).

frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print("Me gusta la", fruta)


leyenda = "Ho#la Cl#ase! Como va to#do, el prese#ntismo esta abierto ahora!!"
for caracter in leyenda: 
    if caracter == "#":
        continue
    print(f"{caracter.upper()}", end="")
    if caracter == "!":
        print()
        break

# Sintaxis

# for iterable in secuencia:
#     sentencia1
#     sentencia1
#     sentencian


# for (i=0; i < 10; i=i+1) {

# }

# La función range() genera una secuencia de números.
# Se puede utilizar junto con la sentencia for para iterar una cantidad específica de veces.


# range(a1) numeros enteros desde 0 hasta a1-1
# range(a1,a2) numeros enteros desde a1 hasta a2-1
# range(a1,a2,a3) numeros enteros desde 0 hasta a1 hasta a2-1 incrementando de a3


print("TABLA De Multiplicar del 3")
for i in range(0,11): # 0 al 10 0 - 1 - 2 - .... 10
    res = 3 * i
    print(f"0{i}X 3 = {res}")
