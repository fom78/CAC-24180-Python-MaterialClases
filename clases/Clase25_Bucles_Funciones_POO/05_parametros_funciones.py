def multiplicar(a, b):
    """
    Esta función recibe dos números como parámetros y devuelve su producto.
    
    Parámetros:
    a (int, float): El primer número.
    b (int, float): El segundo número.
    
    Retorna:
    int, float: El producto de a y b.
    """
    return a * b

# Llamada a la función multiplicar
resultado = multiplicar(5, 4)
print("El producto es:", resultado)  # Salida: El producto es: 20


# Función para agregar una película
def agregar_pelicula(titulo, release_year, es_adulto=False):
    """
    Esta función crea un diccionario que representa una película.

    :param titulo: Título de la película
    :param release_year: Año de lanzamiento de la película
    :param es_adulto: Indicador de si la película es para adultos (opcional, por defecto es False)
    :return: Diccionario con la información de la película
    """
    # Creamos un diccionario con la información de la película usando los parámetros recibidos
    pelicula = {
        "titulo": titulo,
        "release_year": release_year,
        "es_adulto": es_adulto
    }
    # Devolvemos el diccionario que representa la película
    return pelicula

# Ahora, vamos a usar la función para agregar algunas películas

# Agregar una película usando solo los parámetros obligatorios
pelicula1 = agregar_pelicula("The Matrix", 1999)
# La variable 'pelicula1' ahora contiene un diccionario con la información de la película 'The Matrix'

# Agregar una película usando todos los parámetros, incluyendo el opcional 'es_adulto'
pelicula2 = agregar_pelicula("Inception", 2010, es_adulto=True)
# La variable 'pelicula2' ahora contiene un diccionario con la información de la película 'Inception'

# Imprimimos la información de las películas para verificar los resultados
print("Película 1:", pelicula1)


print("Película 2:", pelicula2)

