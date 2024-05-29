# cadenas.py

# Cadenas de caracteres
# Una cadena es una secuencia de caracteres. Se define utilizando comillas simples o dobles.

mensaje = "Hola, Mundo"
print(mensaje)  # Salida: Hola, Mundo

# Métodos de cadenas
# Los métodos de cadenas son funciones integradas que se pueden usar con cadenas.

# Convertir a mayúsculas
mensaje_mayusculas = mensaje.upper()
print(mensaje_mayusculas)  # Salida: HOLA, MUNDO

# Convertir a minúsculas
mensaje_minusculas = mensaje.lower()
print(mensaje_minusculas)  # Salida: hola, mundo

# Reemplazar parte de la cadena
mensaje_reemplazado = mensaje.replace("Mundo", "Python")
print(mensaje_reemplazado)  # Salida: Hola, Python

# f-strings
# Las f-strings (formatted strings) permiten insertar expresiones dentro de cadenas de una manera sencilla.

nombre = "Fernando"
edad = 45
presentacion = f"Hola, mi nombre es {nombre} y tengo {edad} años."
print(presentacion)  # Salida: Hola, mi nombre es Juan y tengo 30 años.

# Índices y slicing (rebanadas)
# Los índices permiten acceder a caracteres individuales en una cadena. El índice comienza en 0.

primera_letra = mensaje[0]
print(primera_letra)  # Salida: H

# El slicing permite obtener subcadenas especificando un rango de índices.
subcadena = mensaje[0:4]  # Incluye caracteres desde el índice 0 hasta el 3
print(subcadena)  # Salida: Hola

# Si omites el índice de inicio o fin, Python usa el inicio o fin de la cadena por defecto.
subcadena_inicio = mensaje[:4]
print(subcadena_inicio)  # Salida: Hola

subcadena_fin = mensaje[5:]
print(subcadena_fin)  # Salida: Mundo
