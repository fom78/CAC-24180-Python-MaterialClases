
# Funciones Lambda/Anónima
# Una función lambda es una pequeña función anónima.
# Puede tener cualquier número de argumentos, pero solo una expresión.
# La expresión se evalúa y se devuelve.

# Definición de una función lambda
suma = lambda x, y: x + y

# Llamada a la función lambda
resultado_lambda = suma(2, 3)
print("La suma usando lambda es:", resultado_lambda)  # Salida: La suma usando lambda es: 5

# Uso de funciones lambda con funciones integradas
# Por ejemplo, con la función sorted()
puntos = [(1, 2), (3, 1), (5, 0), (2, 4)]
# Ordenar por la segunda coordenada
puntos_ordenados = sorted(puntos, key=lambda punto: punto[1])
print("Puntos ordenados por la segunda coordenada:", puntos_ordenados)  # Salida: [(5, 0), (3, 1), (1, 2), (2, 4)]

movies = [
    {
        "title": "The Shawshank Redemption",
        "release_year": 1994,
        "adult": False
    },
    {
        "title": "The Godfather",
        "release_year": 1972,
        "adult": False
    },
    {
        "title": "The Dark Knight",
        "release_year": 2008,
        "adult": True
    },
    {
        "title": "Pulp Fiction",
        "release_year": 1994,
        "adult": True
    },
    {
        "title": "Schindler's List",
        "release_year": 1993,
        "adult": False
    },
    {
        "title": "The Lord of the Rings: The Return of the King",
        "release_year": 2003,
        "adult": False
    },
    {
        "title": "Forrest Gump",
        "release_year": 1994,
        "adult": False
    },
    {
        "title": "Inception",
        "release_year": 2010,
        "adult": False
    },
    {
        "title": "Fight Club",
        "release_year": 1999,
        "adult": True
    },
    {
        "title": "The Matrix",
        "release_year": 1999,
        "adult": True
    }
]

# Caso muy interesante de uso, para ordenar listas de diccionarios, por el valor de una clave.
# Ordenar por release_year

sorted_movies = sorted(movies, key=lambda x: (x['release_year']))

# Mostrar la lista ordenada
for movie in sorted_movies:
    print(movie)