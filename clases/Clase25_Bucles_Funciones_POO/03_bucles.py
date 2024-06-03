# Iterativas: sentencia while y for
# Las sentencias iterativas se utilizan para repetir un bloque de código varias veces.

# Sentencia while
# Se ejecuta mientras una condición sea verdadera.

contador = 0
while contador < 5:
    print("El contador es:", contador)
    contador += 1

# Sentencia for
# Se utiliza para iterar sobre una secuencia (por ejemplo, una lista o una cadena).

frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print("Me gusta la", fruta)

# La función range() genera una secuencia de números.
# Se puede utilizar junto con la sentencia for para iterar una cantidad específica de veces.

for i in range(5):
    print("Número:", i)
