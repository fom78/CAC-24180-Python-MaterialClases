# Funciones: Concepto
# Una función es un bloque de código que solo se ejecuta cuando se le llama.
# Puedes pasar datos, conocidos como parámetros, a una función.
# Una función puede devolver datos como resultado.

# Definición de una función
def saludar():
    """
    Esta función imprime un saludo en la pantalla.
    """
    print("¡Hola, Mundo!")

# Llamada a una función
saludar()  # Salida: ¡Hola, Mundo!

# Función con parámetros y retorno de valores
def sumar(a, b):
    """
    Esta función recibe dos números como parámetros y devuelve su suma.
    """
    res = a+b
    return res

dd = (2,5,7)
dd2 = 2,5,7
# Llamada a la función con argumentos
resultado = sumar(3, 4)
print("La suma es:", resultado)  # Salida: La suma es: 7
