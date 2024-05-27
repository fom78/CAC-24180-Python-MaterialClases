# introduccion_y_ambiente.py

# Introducción a Python:
# Python es un lenguaje de programación de alto nivel, interpretado y de propósito general.
# Es conocido por su sintaxis sencilla y su legibilidad, lo que facilita su aprendizaje y uso.

# Entorno de desarrollo:
# Para escribir y ejecutar programas en Python, puedes usar un IDE (Entorno de Desarrollo Integrado) como:
# - PyCharm
# - VSCode
# - Jupyter Notebook
# También puedes ejecutar scripts de Python directamente desde la línea de comandos.

# Nuestro primer programa: "Hola, Mundo"
# Este es el programa más básico en cualquier lenguaje de programación y simplemente imprime un mensaje en la pantalla.

# Imprimir "Hola, Mundo" en la pantalla
print("Hola, Mundo")



# Comentarios
# Los comentarios son líneas de texto que no se ejecutan como código.
# Sirven para explicar y documentar el código.

# Comentarios en línea
# Se usan para explicar una línea específica de código.
# Por ejemplo, aquí estamos imprimiendo un mensaje:
print("Esto es un comentario en línea")  # Este es un comentario en línea

# Comentarios en bloque
# Se usan para explicar una sección más grande de código.
# Generalmente se colocan antes de la sección de código a la que se refieren.
# Por ejemplo:
'''
Este es un comentario en bloque.
Puede abarcar múltiples líneas.
Se usa para describir una sección más grande de código o proporcionar información adicional.
'''

# Docstrings
# Los docstrings son una forma especial de comentario que se usa para documentar funciones, clases y módulos.
# Se colocan entre comillas triples (""") y pueden abarcar múltiples líneas.
# Por ejemplo, aquí tenemos una función con un docstring:

def saludo():
    """
    Esta función imprime un saludo en la pantalla.
    Es un ejemplo de cómo usar docstrings para documentar una función.
    """
    print("Hola desde la función 'saludo'")

# Llamamos a la función para ver el saludo en la pantalla
saludo()