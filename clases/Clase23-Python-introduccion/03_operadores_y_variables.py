# operadores_y_variables.py

# Variables
# Una variable es un espacio en la memoria que se usa para almacenar un valor.
# Puedes asignar un valor a una variable utilizando el operador de asignación (=).

# Asignación de variables
a = 5
b = 3.2
c = "¡Hola!"

# Imprimir las variables
print("Valor de a:", a)
print("Valor de b:", b)
print("Valor de c:", c)

# Operadores aritméticos
# Los operadores aritméticos se usan para realizar operaciones matemáticas.
# Aquí hay algunos ejemplos:
suma = a + b  # Suma
resta = a - b  # Resta
multiplicacion = a * b  # Multiplicación
division = a / b  # División
modulo = a % 2  # Módulo (resto de la división)
potencia = a ** 2  # Potencia

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("Módulo:", modulo)
print("Potencia:", potencia)

# Operadores de asignación
# Los operadores de asignación se usan para asignar valores a las variables.
# El operador de asignación más básico es `=`, pero hay otros que combinan
# operaciones aritméticas con la asignación.
x = 10
x += 5  # Equivalente a x = x + 5
print("Valor de x después de += 5:", x)

x -= 3  # Equivalente a x = x - 3
print("Valor de x después de -= 3:", x)

x *= 2  # Equivalente a x = x * 2
print("Valor de x después de *= 2:", x)

x /= 4  # Equivalente a x = x / 4
print("Valor de x después de /= 4:", x)

# Operadores de pertenencia
# Los operadores de pertenencia se usan para verificar si un valor o variable
# se encuentra dentro de una secuencia (como una cadena, lista, tupla, etc.).
# Los operadores de pertenencia son `in` y `not in`.

# Ejemplos de operadores de pertenencia:
cadena = "Hola, Python"
lista = [1, 2, 3, 4, 5]

# Uso de `in`
print("Python" in cadena)  # Devuelve True si "Python" está en la cadena
print(3 in lista)  # Devuelve True si 3 está en la lista

# Uso de `not in`
print("Java" not in cadena)  # Devuelve True si "Java" no está en la cadena
print(6 not in lista)  # Devuelve True si 6 no está en la lista
