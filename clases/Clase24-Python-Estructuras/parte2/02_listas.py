# listas.py

# Listas
# Una lista es una colección ordenada y modificable. Permite elementos duplicados.
# Se define utilizando corchetes [].

numeros = [1, 2, 3, 4, 5]
print(numeros)  # Salida: [1, 2, 3, 4, 5]

# Métodos de listas
# Los métodos de listas son funciones integradas que se pueden usar con listas.

# Añadir un elemento al final de la lista
numeros.append(6)
print(numeros)  # Salida: [1, 2, 3, 4, 5, 6]

# Insertar un elemento en una posición específica
numeros.insert(2, 2.5)
print(numeros)  # Salida: [1, 2, 2.5, 3, 4, 5, 6]

# Eliminar un elemento de la lista
numeros.remove(2.5)
numeros.pop(45)
print(numeros)  # Salida: [1, 2, 3, 4, 5, 6]

# Ordenar la lista
numeros.sort()
print(numeros)  # Salida: [1, 2, 3, 4, 5, 6]

# Tipo de datos compuestos
# Las listas pueden contener elementos de diferentes tipos, incluyendo otras listas.

mixta = [1, "dos", 3.0, [4, 5]]
print(mixta)  # Salida: [1, "dos", 3.0, [4, 5]]
