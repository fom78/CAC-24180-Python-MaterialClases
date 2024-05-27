# salida_entrada_y_tipos_de_datos.py

# Salida por pantalla: print
# La función `print` se usa para mostrar información en la pantalla.
print("Este es un mensaje en la pantalla")

# Lectura por teclado: input
# La función `input` se usa para leer datos ingresados por el usuario.
# Por defecto, los datos ingresados por `input` son de tipo ➡️ string.
nombre = input("Ingresa tu nombre: ")
print("Hola, " + nombre)

# Tipos de datos
# En Python, los tipos de datos más comunes son:
# - Números enteros (int)
# - Números flotantes (float)
# - Texto (str)
# - Booleanos (bool)

# Ejemplos de tipos de datos:
numero_entero = 10  # int
numero_flotante = 3.14  # float
texto = "Python es genial"  # str
booleano = True  # bool

# Imprimir los valores y sus tipos
print("Número entero:", numero_entero, "de tipo", type(numero_entero))
print("Número flotante:", numero_flotante, "de tipo", type(numero_flotante))
print("Texto:", texto, "de tipo", type(texto))
print("Booleano:", booleano, "de tipo", type(booleano))
