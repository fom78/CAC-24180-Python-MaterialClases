# estructuras_de_datos.py

# Listas, Tuplas y Diccionarios
# Estas son algunas de las estructuras de datos más utilizadas en Python para almacenar colecciones de elementos.
"hjshsdfh"
# Listas
# Una lista es una colección ordenada y modificable. Permite elementos duplicados.
# Se define utilizando corchetes [].

# Ejemplo de lista
frutas = ["manzana", "banana", "cereza", 67, True, True, False]

# Accediendo a elementos de la lista
print("Primera fruta:", frutas[0])  # Salida: manzana

# Modificando elementos de la lista
frutas[1] = "kiwi"
print("Lista de frutas modificada:", frutas)  # Salida: ["manzana", "kiwi", "cereza"]

# Añadiendo elementos a la lista
frutas.append("naranja")
print("Lista de frutas con nueva fruta:", frutas)  # Salida: ["manzana", "kiwi", "cereza", "naranja"]

# Tuplas
# Una tupla es una colección ordenada e inmutable. No se pueden modificar, agregar o eliminar elementos después de su creación.
# Se define utilizando paréntesis ().

# Ejemplo de tupla
colores = ("rojo", "verde", "azul")

# Accediendo a elementos de la tupla
print("Segundo color:", colores[1])  # Salida: verde

# Diccionarios
# Un diccionario es una colección desordenada, modificable e indexada. Almacena pares clave-valor.
# Se define utilizando llaves {}.

# Ejemplo de diccionario
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Buenos Aires"
}

# Accediendo a elementos del diccionario
print("Nombre de la persona:", persona["nombre"])  # Salida: Juan

# Modificando elementos del diccionario
persona["edad"] = 35
print("Edad de la persona modificada:", persona["edad"])  # Salida: 35

# Añadiendo nuevos elementos al diccionario
persona["profesion"] = "Ingeniero"
print("Diccionario de persona con nueva clave:", persona)  # Salida: {'nombre': 'Juan', 'edad': 35, 'ciudad': 'Buenos Aires', 'profesion': 'Ingeniero'}
