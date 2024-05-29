# parametros_funciones.py

# Parámetros y argumentos
# Los parámetros son variables listadas dentro de los paréntesis en la definición de una función.
# Los argumentos son los valores que se envían a la función cuando se llama.

# Parámetros por valor (inmutables)
def duplicar_valor(x):
    """
    Esta función intenta duplicar el valor de x.
    """
    x = x * 2
    return x

valor = 10
nuevo_valor = duplicar_valor(valor)
print("Valor original:", valor)  # Salida: Valor original: 10
print("Nuevo valor:", nuevo_valor)  # Salida: Nuevo valor: 20

# Parámetros por referencia (mutables)
def duplicar_elementos(lista):
    """
    Esta función duplica cada elemento en la lista.
    """
    for i in range(len(lista)):
        lista[i] *= 2

mi_lista = [1, 2, 3]
duplicar_elementos(mi_lista)
print("Lista después de duplicar elementos:", mi_lista)  # Salida: Lista después de duplicar elementos: [2, 4, 6]

# Parámetros por defecto
def saludar(nombre="Mundo"):
    """
    Esta función saluda a la persona cuyo nombre se pasa como argumento. Si no se pasa ningún nombre, saluda al 'Mundo'.
    """
    print(f"¡Hola, {nombre}!")

saludar()  # Salida: ¡Hola, Mundo!
saludar("Juan")  # Salida: ¡Hola, Juan!
