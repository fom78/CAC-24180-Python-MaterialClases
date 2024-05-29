"""
asientos_disponibles = int(input('Ingrese la cantidad de asientos disponibles: '))
if asientos_disponibles < 10:
    print('Quedan pocos asientos!')
else:
    print('Quedan muchos asientos aun!')

edad = int(input('Ingrese su edad: '))
if edad < 12:
    precio = 500
elif 12 <= edad <= 18:
    precio = 900
elif 18 < edad <= 65:
    precio = 1500
else:
    precio = 1000
print(f"El precio del ticket es: {precio}")


cantidad_ticket = int(input("Ingrese la cantidad de tickets que va a  comprar: "))
precio_base = 1500
if cantidad_ticket > 5:
    precio_final = cantidad_ticket * precio_base * 0.9
else:
    precio_final = cantidad_ticket * precio_base
print(f"El precio final es: {precio_final}")


"""

