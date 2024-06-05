# Definición del decorador
def decorador_mensaje(func):
    def funcion_decorada(*args, **kwargs):
        print("Llamando a la función...")
        resultado = func(*args, **kwargs)  # Llamar a la función original con todos sus argumentos
        print("Función llamada con éxito")
        return resultado
    return funcion_decorada

# Aplicar el decorador a la función original usando @
@decorador_mensaje
def saludar(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}!")

# Llamar a la función decorada
saludar("Mundo")
saludar("Estudiante", saludo="Bienvenido")
