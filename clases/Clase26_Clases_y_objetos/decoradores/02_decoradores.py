"""
Los decoradores en Python son funciones que toman otra función como argumento y extienden o agregan funcionalidad a esa función sin modificar su implementación original. Esto permite modificar o ampliar el comportamiento de una función sin tener que modificar su código interno. Los decoradores son comunes en Python y se utilizan para realizar tareas como la validación de entrada, el registro de actividad, la gestión de la caché, entre otros.

Concepto de Decoradores:
Los decoradores se definen utilizando la sintaxis @decorator_name justo encima de la definición de una función. Cuando se llama a la función decorada, en realidad se está llamando al decorador que se pasa como argumento, y el resultado de la función decoradora es la función modificada o envuelta. Los decoradores son funciones de orden superior que pueden aceptar y devolver funciones.

"""

def decorador_mensaje(func):
    def funcion_decorada():
        print("Llamando a la función...")
        func()  # Llamar a la función original
        print("Función llamada con éxito")
    return funcion_decorada

# Función original
def saludar():
    print("Hola!")

# Aplicar el decorador a la función original
saludar_decorada = decorador_mensaje(saludar)

# Llamar a la función decorada
saludar_decorada()


"""
# Aplicar el decorador a la función original usando @
@decorador_mensaje
def saludar():
    print("Hola!")

# Llamar a la función decorada
saludar()
"""